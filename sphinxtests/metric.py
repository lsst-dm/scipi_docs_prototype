# See COPYRIGHT file at the top of the source tree.
from __future__ import print_function, division
from past.builtins import basestring

import operator
from collections import OrderedDict
import yaml


__all__ = ['Metric', 'load_metrics']


class Metric():
    """Container for the definition of a metric and its specification levels.

    Metrics can either be instantiated programatically, or from a :ref:`metric
    YAML file <validate-base-metric-yaml>` with the `from_yaml` class method.

    .. seealso::

       See the :ref:`validate-base-using-metrics` page for usage details.

    Parameters
    ----------
    name : `str`
        Name of the metric (e.g., ``'PA1'``).
    description : `str`
        Short description about the metric.
    operator_str : `str`
        A string, such as ``'<='``, that defines a success test for a
        measurement (on the left hand side) against the metric specification
        level (right hand side).
    specs : `list`, optional
        A `list` of `Specification` objects that define various specification
        levels for this metric.
    parameters : `dict`, optional
        A `dict` of named `Datum` values that must be known when measuring
        a metric.
    reference_doc : `str`, optional
        The document handle that originally defined the metric
        (e.g., ``'LPM-17'``).
    reference_url : `str`, optional
        The document's URL.
    reference_page : `str`, optional
        Page where metric in defined in the reference document.
    """

    name = None
    """Name of the metric (`str`)."""

    description = None
    """Short description of the metric (`str`)."""

    reference_doc = None
    """Name of the document that specifies this metric (`str`)."""

    reference_url = None
    """URL of the document that specifies this metric (`str`)."""

    reference_page = None
    """Page number in the document that specifies this metric (`int`)."""

    parameters = dict()
    """`dict` of named :class:`Datum` values that must be known when measuring
    a metric.

    Parameters can also be accessed as attributes of the metric. Attribute
    names are the same as key names in `parameters`.
    """

    def __init__(self, name, description, operator_str,
                 specs=None, parameters=None,
                 reference_doc=None, reference_url=None, reference_page=None):
        self.name = name
        self.description = description
        self.reference_doc = reference_doc
        self.reference_url = reference_url
        self.reference_page = reference_page

        self.operator_str = operator_str

        if specs is None:
            self.specs = []
        else:
            self.specs = specs

        if parameters is None:
            self.parameters = {}
        else:
            assert isinstance(parameters, dict)
            for key, value in parameters.items():
                assert isinstance(key, basestring)
                assert isinstance(value, Datum)
            self.parameters = parameters

    @classmethod
    def from_yaml(cls, metric_name, yaml_doc=None, yaml_path=None,
                  resolve_dependencies=True):
        """Create a `Metric` instance from a YAML document that defines
        metrics.

        .. seealso::

           See :ref:`validate-base-metric-yaml` for details on the metric YAML
           schema.

        Parameters
        ----------
        metric_name : `str`
            Name of the metric (e.g., ``'PA1'``).
        yaml_doc : `dict`, optional
            A full metric YAML document loaded as a `dict`. Use this option
            to increase performance by eliminating redundant reads of a
            common metric YAML file. Alternatively, set ``yaml_path``.
        yaml_path : `str`, optional
            The full file path to a metric YAML file. Alternatively, set
            ``yaml_doc``.
        resolve_dependencies : `bool`, optional
            API users should always set this to `True`. The opposite is used
            only used internally.

        Raises
        ------
        RuntimeError
            Raised when neither ``yaml_doc`` or ``yaml_path`` are set.
        """
        if yaml_doc is None and yaml_path is not None:
            with open(yaml_path) as f:
                yaml_doc = yaml.load(f)
        elif yaml_doc is None and yaml_path is None:
            raise RuntimeError('Set either yaml_doc or yaml_path argument')
        metric_doc = yaml_doc[metric_name]

        metric_params = {}
        if 'parameters' in metric_doc:
            for param_name, param_data in metric_doc['parameters'].items():
                d = Datum(param_data['value'],
                          param_data.get('unit', ''),
                          label=param_data.get('label', None),
                          description=param_data.get('description', None))
                metric_params[param_name] = d

        m = cls(
            metric_name,
            description=metric_doc.get('description', None),
            operator_str=metric_doc['operator'],
            reference_doc=metric_doc['reference'].get('doc', None),
            reference_url=metric_doc['reference'].get('url', None),
            reference_page=metric_doc['reference'].get('page', None),
            parameters=metric_params)

        for spec_doc in metric_doc['specs']:
            deps = None
            if 'dependencies' in spec_doc and resolve_dependencies:
                deps = {}
                for dep_item in spec_doc['dependencies']:
                    if isinstance(dep_item, basestring):
                        # This is a metric
                        name = dep_item
                        d = Metric.from_yaml(name, yaml_doc=yaml_doc,
                                             resolve_dependencies=False)
                    elif isinstance(dep_item, dict):
                        # Likely a Datum
                        # in yaml, wrapper object is dict with single key-val
                        name = list(dep_item.keys())[0]
                        dep_item = dict(dep_item[name])
                        v = dep_item['value']
                        unit = dep_item['unit']
                        d = Datum(v, unit,
                                  label=dep_item.get('label', None),
                                  description=dep_item.get('description', None))
                    else:
                        raise RuntimeError(
                            'Cannot process dependency %r' % dep_item)
                    deps[name] = d
            spec = Specification(name=spec_doc['level'],
                                 quantity=spec_doc['value'],
                                 unit=spec_doc['unit'],
                                 filter_names=spec_doc.get('filter_names', None),
                                 dependencies=deps)
            m.specs.append(spec)

        return m

    @classmethod
    def from_json(cls, json_data):
        """Construct a Metric from a JSON dataset.

        Parameters
        ----------
        json_data : `dict`
            Metric JSON object.

        Returns
        -------
        metric : `Metric`
            Metric from JSON.
        """
        specs = [Specification.from_json(v)
                 for v in json_data['specifications']]
        params = {k: Datum.from_json(v)
                  for k, v in json_data['parameters'].items()}
        m = cls(json_data['name'],
                json_data['description'],
                json_data['operator_str'],
                specs=specs,
                parameters=params,
                reference_doc=json_data['reference']['doc'],
                reference_page=json_data['reference']['page'],
                reference_url=json_data['reference']['url'])
        return m

    def __getattr__(self, key):
        if key in self.parameters:
            return self.parameters[key]
        else:
            raise AttributeError("%r object has no attribute %r" %
                                 (self.__class__, key))

    @property
    def reference(self):
        """Documentation reference as human-readable text (`str`, read-only).

        Uses `reference_doc`, `reference_page`, and `reference_url`, as
        available.
        """
        ref_str = ''
        if self.reference_doc and self.reference_page:
            ref_str = '{doc}, p. {page:d}'.format(doc=self.reference_doc,
                                                  page=self.reference_page)
        elif self.reference_doc:
            ref_str = self.reference_doc

        if self.reference_url and self.reference_doc:
            ref_str += ', {url}'.format(url=self.reference_url)
        elif self.reference_url:
            ref_str = self.reference_url

        return ref_str

    @property
    def operator_str(self):
        """String representation of comparison operator.

        The comparison is oriented with the measurement on the left-hand side
        and the specification level on the right-hand side.
        """
        return self._operator_str

    @operator_str.setter
    def operator_str(self, v):
        # Cache the operator function as a means of validating the input too
        self._operator = Metric.convert_operator_str(v)
        self._operator_str = v

    @property
    def operator(self):
        """Binary comparision operator that tests success of a measurement
        fulfilling a specification of this metric.

        Measured value is on left side of comparison and specification level
        is on right side.
        """
        return self._operator

    @staticmethod
    def convert_operator_str(op_str):
        """Convert a string representing a binary comparison operator to
        the operator function itself.

        Operators are oriented so that the measurement is on the left-hand
        side, and specification level on the right hand side.

        The following operators are permitted:

        ========== =============
        ``op_str`` Function
        ========== =============
        ``>=``     `operator.ge`
        ``>``      `operator.gt`
        ``<``      `operator.lt`
        ``<=``     `operator.le`
        ``==``     `operator.eq`
        ``!=``     `operator.ne`
        ========== =============

        Parameters
        ----------
        op_str : `str`
            A string representing a binary operator.

        Returns
        -------
        op_func : obj
            An operator function from the `operator` standard library
            module.
        """
        operators = {'>=': operator.ge,
                     '>': operator.gt,
                     '<': operator.lt,
                     '<=': operator.le,
                     '==': operator.eq,
                     '!=': operator.ne}
        return operators[op_str]

    def get_spec(self, name, filter_name=None):
        """Get a specification by name and other qualifications.

        Parameters
        ----------
        name : `str`
            Name of a specification level (e.g., ``'design'``, ``'minimum'``,
            ``'stretch'``).
        filter_name : `str`, optional
            The name of the optical filter to qualify a filter-dependent
            specification level.

        Returns
        -------
        spec : `Specification`
            The `Specification` that matches the name and other qualifications.

        Raises
        ------
        RuntimeError
           If a specification cannot be found.
        """
        # First collect candidate specifications by name
        candidates = [s for s in self.specs if s.name == name]
        if len(candidates) == 1:
            return candidates[0]

        # Filter down by optical filter
        if filter_name is not None:
            candidates = [s for s in candidates
                          if filter_name in s.filter_names]
        if len(candidates) == 1:
            return candidates[0]

        raise RuntimeError(
            'No {2} spec found for name={0} filter_name={1}'.format(
                name, filter_name, self.name))

    def get_spec_dependency(self, spec_name, dep_name, filter_name=None):
        """Get the `Datum` of a specification's dependency.

        If the dependency is a metric, this method resolves the value of the
        dependent metric's specification level ``spec_name``. In other words,
        ``spec_name`` refers to the specification level of both *this* metric
        and of the dependency metric.

        Parameters
        ----------
        spec_name : `str`
            `Specification` name.
        dep_name : `str`
            Name of the dependency.
        filter_name : `str`, optional
            Name of the optical filter, if this metric's specifications are
            optical filter dependent.

        Returns
        -------
        datum : `Datum`
            The dependency resolved for the metric's specification.
        """
        spec = self.get_spec(spec_name, filter_name=filter_name)
        dep = spec.dependencies[dep_name]
        if isinstance(dep, Metric):
            dep_spec = dep.get_spec(spec_name, filter_name=filter_name)
            return dep_spec.datum
        else:
            # The dependency should be a straight Datum
            assert isinstance(dep, Datum) is True
            return dep

    def get_spec_names(self, filter_name=None):
        """List names of all specification levels defined for this metric;
        optionally filtering by attributes such as filter name.

        Parameters
        ----------
        filter_name : `str`, optional
            Name of the applicable filter, if needed.

        Returns
        -------
        spec_names : `list`
            Specification names as a list of strings,
            e.g. ``['design', 'minimum', 'stretch']``.
        """
        spec_names = []

        for spec in self.specs:
            if (filter_name is not None) and (spec.filter_names is not None) \
                    and (filter_name not in spec.filter_names):
                continue
            spec_names.append(spec.name)

        return list(set(spec_names))

    def check_spec(self, quantity, spec_name, filter_name=None):
        """Compare a measurement against a named specification level.

        Parameters
        ----------
        value : `astropy.units.Quantity`
            The measurement value.
        spec_name : `str`
            Name of a `Specification` associated with this metric.
        filter_name : `str`, optional
            Name of the applicable filter, if needed.

        Returns
        -------
        passed : `bool`
            `True` if the value meets the specification, `False` otherwise.
        """
        spec = self.get_spec(spec_name, filter_name=filter_name)
        return self.operator(quantity, spec.quantity)

    @property
    def json(self):
        """`dict` that can be serialized as semantic JSON, compatible with
        the SQUASH metric service.
        """
        ref_doc = {
            'doc': self.reference_doc,
            'page': self.reference_page,
            'url': self.reference_url}
        return JsonSerializationMixin.jsonify_dict({
            'name': self.name,
            'operator_str': self.operator_str,
            'reference': ref_doc,
            'description': self.description,
            'specifications': self.specs,
            'parameters': self.parameters})


def load_metrics(yaml_path):
    """Load metric from a YAML document into an ordered dictionary of
    `Metric`\ s.

    .. seealso::

       :ref:`validate-base-metric-yaml`.

    Parameters
    ----------
    yaml_path : `str`
        The full file path to a metric YAML file.

    Returns
    -------
    metrics : `collections.OrderedDict`
        A dictionary of `Metric` instances, ordered to matched layout of YAML
        document at YAML path. Keys are names of metrics (`str`).

    See also
    --------
    Metric.from_yaml
        Make a single `Metric` instance from a YAML document.
    """
    with open(yaml_path) as f:
        metrics_doc = _load_ordered_yaml(f)
    metrics = []
    for key in metrics_doc:
        metrics.append((key, Metric.from_yaml(key, metrics_doc)))
    return OrderedDict(metrics)


def _load_ordered_yaml(stream, Loader=yaml.Loader,
                       object_pairs_hook=OrderedDict):
    """Load a YAML document into an OrderedDict

    Solution from http://stackoverflow.com/a/21912744
    """
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)

    return yaml.load(stream, OrderedLoader)
