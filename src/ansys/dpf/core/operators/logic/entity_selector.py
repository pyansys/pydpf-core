"""
entity_selector
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class entity_selector(Operator):
    """Creates a scalar/vector field based on the selected entity.

    Parameters
    ----------
    field : Field or FieldsContainer
    entity_number : int
        One or several entity index that will be
        extracted from the initial field.
    default_value : float, optional
        Set a default value for entity that do not
        exist.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.logic.entity_selector()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_entity_number = int()
    >>> op.inputs.entity_number.connect(my_entity_number)
    >>> my_default_value = float()
    >>> op.inputs.default_value.connect(my_default_value)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.logic.entity_selector(
    ...     field=my_field,
    ...     entity_number=my_entity_number,
    ...     default_value=my_default_value,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self,
        field=None,
        entity_number=None,
        default_value=None,
        config=None,
        server=None,
    ):
        super().__init__(name="entity_selector", config=config, server=server)
        self._inputs = InputsEntitySelector(self)
        self._outputs = OutputsEntitySelector(self)
        if field is not None:
            self.inputs.field.connect(field)
        if entity_number is not None:
            self.inputs.entity_number.connect(entity_number)
        if default_value is not None:
            self.inputs.default_value.connect(default_value)

    @staticmethod
    def _spec():
        description = """Creates a scalar/vector field based on the selected entity."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field", "fields_container"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="entity_number",
                    type_names=["int32", "vector<int32>"],
                    optional=False,
                    document="""One or several entity index that will be
        extracted from the initial field.""",
                ),
                2: PinSpecification(
                    name="default_value",
                    type_names=["double"],
                    optional=True,
                    document="""Set a default value for entity that do not
        exist.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
            },
        )
        return spec

    @staticmethod
    def default_config(server=None):
        """Returns the default config of the operator.

        This config can then be changed to the user needs and be used to
        instantiate the operator. The Configuration allows to customize
        how the operation will be processed by the operator.

        Parameters
        ----------
        server : server.DPFServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(name="entity_selector", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsEntitySelector
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsEntitySelector
        """
        return super().outputs


class InputsEntitySelector(_Inputs):
    """Intermediate class used to connect user inputs to
    entity_selector operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.entity_selector()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_entity_number = int()
    >>> op.inputs.entity_number.connect(my_entity_number)
    >>> my_default_value = float()
    >>> op.inputs.default_value.connect(my_default_value)
    """

    def __init__(self, op: Operator):
        super().__init__(entity_selector._spec().inputs, op)
        self._field = Input(entity_selector._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._entity_number = Input(entity_selector._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._entity_number)
        self._default_value = Input(entity_selector._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._default_value)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        Parameters
        ----------
        my_field : Field or FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.entity_selector()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def entity_number(self):
        """Allows to connect entity_number input to the operator.

        One or several entity index that will be
        extracted from the initial field.

        Parameters
        ----------
        my_entity_number : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.entity_selector()
        >>> op.inputs.entity_number.connect(my_entity_number)
        >>> # or
        >>> op.inputs.entity_number(my_entity_number)
        """
        return self._entity_number

    @property
    def default_value(self):
        """Allows to connect default_value input to the operator.

        Set a default value for entity that do not
        exist.

        Parameters
        ----------
        my_default_value : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.entity_selector()
        >>> op.inputs.default_value.connect(my_default_value)
        >>> # or
        >>> op.inputs.default_value(my_default_value)
        """
        return self._default_value


class OutputsEntitySelector(_Outputs):
    """Intermediate class used to get outputs from
    entity_selector operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.logic.entity_selector()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(entity_selector._spec().outputs, op)
        self._field = Output(entity_selector._spec().output_pin(0), 0, op)
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator

        Returns
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.logic.entity_selector()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field