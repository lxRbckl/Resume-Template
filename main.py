# < Resume Template 2 by Alex Arbuckle > #


# import <
from dash import Dash
from framework import framework
from lxrbckl.local import fileGet
from dash_bootstrap_components import themes

# >


# main <
if (__name__ == '__main__'):
    
    data = fileGet(pFile = '/data.json')
    layout = framework().layout(data)
    
    application = Dash(
        
        name = 'Resume',
        title = 'Resume',
        external_stylesheets = [
            
            themes.GRID,
            themes.BOOTSTRAP
            
        ]
        
    )
    application.layout = layout
    application.run(debug = True)

# >