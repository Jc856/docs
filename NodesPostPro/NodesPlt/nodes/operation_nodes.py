from NodeGraphQt import BaseNode
import sys

class DropdownMenuNode(BaseNode):
    """
    An example node with a embedded added QCombobox menu.
    """

    # unique node identifier.
    __identifier__ = 'nodes.widget'

    # initial default node name.
    NODE_NAME = 'menu'

    def __init__(self):
        super(DropdownMenuNode, self).__init__()

        # create input & output ports
        self.add_input('in 1')
        self.add_output('out 1')
        self.add_output('out 2')

        # create the QComboBox menu.
        items = ['item 1', 'item 2', 'item 3']
        self.add_combo_menu('my_menu', 'Menu Test', items=items)


class MultiplyNode(BaseNode):
    """
    A node class with 2 inputs and 2 outputs.
    """

    # unique node identifier.
    __identifier__ = 'nodes.multiply'

    # initial default node name.
    NODE_NAME = 'node Multiply'

    def __init__(self):
        super(MultiplyNode, self).__init__()

        # create node inputs.
        self.add_input('Input Array 1')
        #self.add_input('Input Array 2')

        # create node outputs.
        self.add_output('Output Array')
        
        self.add_text_input('Value', 'Value', tab='widgets')

        self.input_array_1 = None
        #self.input_array_2 = None
        self.float_to_multiply = None
        self.plugged_input_port = None
        self.is_defined = False

        self.output_array = None

        print(self.model.properties.keys())
        print("view", self.view)

    def update_model(self):
        super(MultiplyNode, self).update_model()

        print("update_model")
    
    def update(self):
        super(MultiplyNode, self).update()

        print("update")

    def set_model(self, model):
        super(MultiplyNode, self).set_model()

        print("set_model")

    def set_property(self, name, value, push_undo=True):
        super(MultiplyNode, self).set_property(name, value, push_undo=push_undo)

        if self.is_defined:
            print(self.model.get_property("Value"))
            self.output_array = self.input_array_1 * self.get_property(name)

        self.update_from_input()

        # self.update_from_input()
        print("Set property called")
        
    def on_input_connected(self, in_port, out_port):
        super(MultiplyNode, self).on_input_connected(in_port, out_port)

        self.plugged_input_port = out_port
        # print(type(out_port))

        # print(out_port.node)
        # print(out_port.node())
        # print(out_port.node().output_data_frame)

        self.update_from_input()
        # print(self.model.get_property("Column name"))

        print("on_input_connected", in_port, out_port, self._model.name)
        
    

    def on_input_disconnected(self, in_port, out_port):
        super(MultiplyNode, self).on_input_disconnected(in_port, out_port)

        print("on_input_disconnected", in_port, out_port, self._model.name)

    def update_from_input(self):
        #print("Curent columns names: ",self.view.widgets["Column name"].all_items())

        if self.plugged_input_port == None:
            pass
        else:
            if self.plugged_input_port.node().is_defined:
                if self.input_array_1 != None:
                    self.is_defined = True
                    self.input_array_1 = self.plugged_input_port.node().output_data_frame
                    print(self.input_array_1)
                    #self.columns = list(self.input_data_frame.columns)

                    #self.view.widgets["Column name"].clear() 
                    #self.view.widgets["Column name"].add_items(self.columns)

        if self.is_defined:
            #print("Found property:", self.output_string)
            self.output_array_1 = self.input_array_1 * self.float_to_multiply
            
            #print("Output array :", self.output_array)


        for output_id in range(len(self.outputs())):
            for connected_id in range(len(self.output(output_id).connected_ports())):
                self.output(output_id).connected_ports()[connected_id].node().update_from_input()