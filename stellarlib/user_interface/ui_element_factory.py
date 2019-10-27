

class UIElementFactory(object):

    def __init__(self, ui_control):

        self.ui_control = ui_control

        '''
        to make an element generically
        
        if not self.ui_control.find_node('pop'):
            pop_up.PopUpNode('pop', self.ui_root_node, (x, y), text_image, color)
            self.ui_control.make_ui_model(pop_up.PopUpModel, 'pop')
        
        1)  if there is a model for the node, then its constructor
            - element_id
            - *args, **kwargs for special elements
        
        2)  need the node constructor
            - element_id, parent node, pos
            - any other specialized data should be in the model, we don't want to pass *args to node
            - w, h will either be baked into class as static or dynamically generated from content
              in the model
            - some elements may have baked or static position as well
            
            call the constructor for the node, now the element is in the scene tree
            
        should nodes get all their data from the model if they have a model?
        eg. pop up model is created first and holds a text field
         then node is initialized and it looks in its related model to
         create its text image element
         
        Since we pass in *args and **kwargs to create_ui_element, we can give models that need
        access to the game state references when it is called. But leave this out if not necessary.
        
        Elements that have nested sub elements should hand their own children's creation in their Node
        and Model constructors. See MenuModel, MenuNode.
         
        '''

    def create_ui_element(self, element_module, element_id, parent_node, pos, *args, **kwargs):

        # TODO handle duplicate element ids?
        assert self.ui_control.find_node(element_id) is None

        model_created = self.create_model(element_module, element_id, *args, **kwargs)
        self.create_node(element_module, element_id, parent_node, pos, self.get_model(element_id, model_created))

    def create_model(self, element_module, element_id, *args, **kwargs):

        created = False

        model = element_module.get_model_constructor()
        if model:
            self.ui_control.make_ui_model(model, element_id, *args, **kwargs)
            created = True

        return created

    def get_model(self, element_id, created):

        if created:
            model = self.ui_control.model_manager.get_model(element_id)
        else:
            model = None

        return model

    def create_node(self, element_module, element_id, parent_node, pos, model):

        node = element_module.get_node_constructor()
        node(element_id, parent_node, pos, model=model)
