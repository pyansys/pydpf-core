"""
workflow_to_workflow_topology
=============================
Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class workflow_to_workflow_topology(Operator):
    """Creates a GenericDataContainer based on WorkflowTopology structure
    from a Workflow object, allowing to access its operators, operator
    connections, data connections, and exposed pins.

    Parameters
    ----------
    workflow : Workflow

    Returns
    -------
    workflow_topology : GenericDataContainer

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.serialization.workflow_to_workflow_topology()

    >>> # Make input connections
    >>> my_workflow = dpf.Workflow()
    >>> op.inputs.workflow.connect(my_workflow)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.serialization.workflow_to_workflow_topology(
    ...     workflow=my_workflow,
    ... )

    >>> # Get output data
    >>> result_workflow_topology = op.outputs.workflow_topology()
    """

    def __init__(self, workflow=None, config=None, server=None):
        super().__init__(
            name="workflow_to_workflow_topology", config=config, server=server
        )
        self._inputs = InputsWorkflowToWorkflowTopology(self)
        self._outputs = OutputsWorkflowToWorkflowTopology(self)
        if workflow is not None:
            self.inputs.workflow.connect(workflow)

    @staticmethod
    def _spec():
        description = """Creates a GenericDataContainer based on WorkflowTopology structure
            from a Workflow object, allowing to access its operators,
            operator connections, data connections, and exposed pins."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="workflow",
                    type_names=["workflow"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="workflow_topology",
                    type_names=["generic_data_container"],
                    optional=False,
                    document="""""",
                    name_derived_class=["WorkflowTopology"],
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
        return Operator.default_config(
            name="workflow_to_workflow_topology", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsWorkflowToWorkflowTopology
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsWorkflowToWorkflowTopology
        """
        return super().outputs


class InputsWorkflowToWorkflowTopology(_Inputs):
    """Intermediate class used to connect user inputs to
    workflow_to_workflow_topology operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.workflow_to_workflow_topology()
    >>> my_workflow = dpf.Workflow()
    >>> op.inputs.workflow.connect(my_workflow)
    """

    def __init__(self, op: Operator):
        super().__init__(workflow_to_workflow_topology._spec().inputs, op)
        self._workflow = Input(
            workflow_to_workflow_topology._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._workflow)

    @property
    def workflow(self):
        """Allows to connect workflow input to the operator.

        Parameters
        ----------
        my_workflow : Workflow

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.workflow_to_workflow_topology()
        >>> op.inputs.workflow.connect(my_workflow)
        >>> # or
        >>> op.inputs.workflow(my_workflow)
        """
        return self._workflow


class OutputsWorkflowToWorkflowTopology(_Outputs):
    """Intermediate class used to get outputs from
    workflow_to_workflow_topology operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.workflow_to_workflow_topology()
    >>> # Connect inputs : op.inputs. ...
    >>> result_workflow_topology = op.outputs.workflow_topology()
    """

    def __init__(self, op: Operator):
        super().__init__(workflow_to_workflow_topology._spec().outputs, op)
        self._workflow_topology = Output(
            workflow_to_workflow_topology._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._workflow_topology)

    @property
    def workflow_topology(self):
        """Allows to get workflow_topology output of the operator

        Returns
        ----------
        my_workflow_topology : WorkflowTopology

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.workflow_to_workflow_topology()
        >>> # Connect inputs : op.inputs. ...
        >>> result_workflow_topology = op.outputs.workflow_topology()
        """  # noqa: E501
        return self._workflow_topology