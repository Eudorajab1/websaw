from upytl import SlotTemplate, html as h 

from upytl_standard import HTMLPage, StandardNavBar 
from ..common.common_components import Flash
# flake8: noqa E226

index = {
    HTMLPage(footer_class='custom-footer'):{
        SlotTemplate(Slot='nav'):{
            StandardNavBar(menu={'menu'}, user= {'user'}, buttons={'buttons'}): '',
        },
        SlotTemplate(Slot='flash'):{},
        
        SlotTemplate(Slot='content'):{
            h.Div(Class='box'):{
                h.Div(Class='title is-4'): 'Welcome [[user]] from the default_template_context',
                h.Div(Class='title is-5'): 'This is the mixin index Template',
                h.Div(For='f in msg'):{
                    h.Text():'[[ f ]] : [[msg[f] ]]',
                }
            }    
        }
    }
}

about = {
    HTMLPage(footer_class='custom-footer'):{
        SlotTemplate(Slot='nav'):{
            StandardNavBar(menu={'menu'}, user= {'user'}, buttons={'buttons'}): '',
        },
        SlotTemplate(Slot='flash'):{
            Flash(): {},
        },
        SlotTemplate(Slot='content'):{
            h.Div(Class='section'):{
                h.Div(Class='box'):{
                    h.Div(Class='title is-5'): 'This is the mixin App about Template',
                    h.Div(Class='title is-5'): 'Click on the links below',
                    h.Div(For='f in msg'):{
                        h.A(Class='button is-medium is-fullwidth is-light is-link', href={'msg[f]'}):'[[ f ]] : [[msg[f] ]]',
                    }
                }
            }    
        }
    }
}

upytl_demo = {
    h.Html():{
        h.Head():{
            h.Title():"[[app_get('app_name')]]",
                h.Meta(charset='utf-8'):'',
                h.Link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.1/css/bulma.min.css'):None, 
            },
            h.Body():{
                h.Div(Class='box'):{
                    h.Div(Class='title'):'[[msg]]',
                }
            },    
            h.Footer():{
                h.Div(): 'This is the footer',
            }

        }
    }
