# import <
from dash import dcc, html
import dash_bootstrap_components as dbc

# >


class framework:
    
    def __init__(self):
        '''  '''
        
        self.width = 850
        self.height = 1100
        self.position = 'top'
        self.colorBlack = '#181A1B'
        self.colorWhite = '#F7F5F1'
        self.backgroundImage = None
        self.fontFamily = 'helvetica'
        self.borderBlack = f'1.5px solid {self.colorBlack}'
        self.borderWhite = f'1.5px solid {self.colorWhite}'
        
    
    def layout(self, pData):
        '''  '''
        
        return dbc.Container(
            
            style = {
                                
                'padding' : 25,
                'marginTop' : 15,
                'display' : 'flex',
                'minWidth' : self.width,
                'maxWidth' : self.width,
                'minHeight' : self.height,
                'maxHeight' : self.height,
                'justify-content' : 'center',
                'align-items' : self.position,
                'background' : self.colorWhite,
                
                'backgroundSize' : 'cover',
                'backgroundPosition' : 'center',
                'backgroundImage' : self.backgroundImage
                           
            },
            children = [
                
                dbc.Row(
                    
                    style = {
                                                
                        'margin' : 6,
                        'width' : '100%',
                        'height' : '100%',
                        'textAlign' : 'center'
                        
                    },
                    children = [
                        
                        {
                            
                            'hr' : self.hr,
                            'badge' : self.badge,
                            'title' : self.title,
                            'image' : self.image,
                            'space' : self.space,
                            'markdown' : self.markdown,
                            'subtitle' : self.subtitle
                            
                        }[t](k)
                        
                    for j in i for t, k in j]
                    
                )
                
            for i in pData]
            
        )
        
    
    def hr(self, v): return html.Hr(
        
        style = {
            
            'opacity' : 1,
            'marginTop' : 5,
            'marginBottom' : 5,
            'borderTop' : self.borderBlack
        
        }
    
    )
    
    
    def badge(self, v):
        '''  '''
        
        return html.Div(
            
            className="d-flex flex-wrap",

            style = {
                
                "margin" : -2,
                'padding' : 0,
                'width' : 'auto'
                
            },
            children = [
                
                dbc.Badge(
                    
                    children = i,
                    color = self.colorWhite,
                    style = {
                        
                        'margin' : 2,
                        'color' : self.colorBlack,
                        'verticalAlign' : 'middle',
                        'border' : self.borderBlack
                    
                    }
                    
                )
                
            for i in v]
            
        )
    
    
    def title(self, v):
        '''  '''
        
        return html.H1(
            
            children = v,
            style = {
                
                'padding' : 0,
                'lineHeight' : 1,
                'margin' : '0 0 0 0',
                'textAlign' : 'left',
                'fontFamily' : self.fontFamily,
                **{
                    
                    # name <
                    # other <
                    False : {
                        
                        'fontSize' : '2rem',
                        'fontWeight' : 'bold'
                        
                    },
                    True : {
                        
                        'fontSize' : '2.5rem',
                        'fontWeight' : '200',
                        'fontStyle' : 'italic'
                        
                    }
                    
                    # >
                    
                }[v == 'Alex Arbuckle']
                
            }
            
        )
    
    
    def image(self, v):
        '''  '''
        
        return html.Img(
            
            src = v,
            style = {
                
                "margin" : 0,
                "padding" : 0
                
            }
            
        )
    
    
    def space(self, v):
        '''  '''
        
        return html.Div(
            
            style = {
                
                'marginTop' : 5,
                'marginBottom' : 5
                
            }
            
        )
    
    
    def markdown(self, v):
        '''  '''
        
        return dcc.Markdown(
            
            children = v,
            style = {
                
                'padding' : 0,
                'textAlign' : 'justify',
                'margin' : '0 0 -15px 0',
                'fontFamily' : self.fontFamily
                
            }
            
        )
    
    
    def subtitle(self, v):
        '''  '''
        
        return html.H1(
            
            children = v,
            style = {
                
                'padding' : 0,
                'margin' : '0 0 0 0',
                'textAlign' : 'left',
                'fontWeight' : '100',
                'fontSize' : '1.1rem',
                'fontFamily' : self.fontFamily
                
            }
            
        )