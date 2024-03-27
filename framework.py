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
                            'small' : self.small,
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
            'color' : self.colorBlack,
            'borderTop' : self.borderBlack
        
        }
    
    )
    
    
    def small(
        
        self, 
        v,
        styled = [
            
            'In',
            'Fall',
            'While',
            'Spring',
            'Issued',
            'github.com/ala2q6/CS456-P',
            'github.com/lxRbckl/Project-ASBC'
            
        ]
        
    ):
        '''  '''
        
        return html.Small(
            
            children = v,
            style = {
                
                'margin' : 0,
                'padding' : 0,
                'color' : self.colorBlack,
                'fontFamily' : self.fontFamily,
                **{
                    
                    'In' : {'fontSize' : '0.8rem', 'textAlign' : 'justify'},
                    False : {'fontSize' : '0.8rem', 'textAlign' : 'justify'},
                    'While' : {'fontSize' : '0.8rem', 'textAlign' : 'justify'},
                    'Fall' : {
                        
                        'textAlign' : 'left',
                        'fontWeight' : '900',
                        'fontSize' : '0.7rem'
                    
                    },
                    'Spring' : {
                        
                        'textAlign' : 'left',
                        'fontWeight' : '900',
                        'fontSize' : '0.7rem'
                    
                    },
                    'Issued' : {
                        
                        'textAlign' : 'left',
                        'fontSize' : '0.8rem', 
                        'fontStyle' : 'italic'
                    
                    },
                    'github.com/ala2q6/CS456-P' : {
                        
                        'textAlign' : 'left',
                        'fontWeight' : '900',
                        'fontSize' : '0.8rem',
                        'padding' : '0 0 0 5px',
                        'borderLeft' : self.borderBlack
                        
                    },
                    'github.com/lxRbckl/Project-ASBC' : {
                        
                        'textAlign' : 'left',
                        'fontWeight' : '900',
                        'fontSize' : '0.8rem',
                        'padding' : '0 0 0 5px',
                        'borderLeft' : self.borderBlack
                        
                    }
                                        
                }[v.split(' ')[0] if (v.split(' ')[0] in styled) else False]
                
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
                        'padding' : 3,
                        'color' : self.colorBlack,
                        'verticalAlign' : 'middle',
                        'border' : self.borderBlack
                    
                    }
                    
                )
                
            for i in v]
            
        )
    
    
    def title(
        
        self, 
        v,
        styled = [

            'Alex',            
            'UMKC',
            'CS456',
            'Advantage',
            'Experience',
            'Independent'
            
        ]
    
    ):
        '''  '''
        
        return html.H1(
            
            children = v,
            style = {
                
                'margin' : 0,
                'padding' : 0,
                'lineHeight' : 1,
                'textAlign' : 'left',
                'color' : self.colorBlack,
                'fontFamily' : self.fontFamily,
                **{
                    
                    # specific <
                    # non-specific <
                    'UMKC' : {
                        
                        'marginBottom' : -5,
                        'fontWeight' : '600',
                        'fontSize' : '1.5rem',
                        'fontStyle' : 'italic'
                        
                    },
                    'CS456' : {
                        
                        'fontWeight' : '400',
                        'fontSize' : '1.5rem',
                        'fontStyle' : 'italic'
                        
                    },
                    'Experience' : {
                        
                        'fontSize' : '2rem',
                        'fontWeight' : 'bold',
                        'fontStyle' : 'italic'
                        
                    },
                    'Alex' : {
                        
                        'fontWeight' : '200',
                        'fontSize' : '2.5rem',
                        'fontStyle' : 'italic'
                        
                    },
                    'Advantage' : {
                        
                        'marginBottom' : -5,
                        'fontWeight' : '400',
                        'fontSize' : '1.5rem',
                        'fontStyle' : 'italic'
                        
                    },
                    'Independent' : {
                        
                        'fontWeight' : '400',
                        'fontSize' : '1.5rem',
                        'fontStyle' : 'italic'
                        
                    },
                    False : {
                        
                        'fontSize' : '2rem',
                        'fontWeight' : 'bold'
                        
                    }
                    
                    # >
                    
                }[v.split(' ')[0] if (v.split(' ')[0] in styled) else False]
                
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
                
                'marginTop' : v
                
            }
            
        )
        
    
    def markdown(self, v):
        '''  '''
        
        return dcc.Markdown(
            
            children = v,
            style = {
                
                'padding' : 0,
                'textAlign' : 'justify',
                'margin' : '0 0 -25px 0',
                "color" : self.colorBlack,
                'fontFamily' : self.fontFamily
                                
            }
            
        )
    
    
    def subtitle(
        
        self, 
        v,
        styled = [
            
            'BS',
            'Cum',
            'Other',
            "Dean's",
            'Awards',
            'Kansas',
            'Bachelor',
            'Packages',
            'Languages',
            'University'
            
        ]
    
    ):
        '''  '''
        
        return html.H1(
            
            children = v,
            style = {
                
                'margin' : 0,
                'padding' : 0,
                'textAlign' : 'left',
                'color' : self.colorBlack,
                'fontFamily' : self.fontFamily,
                **{
                    
                    False : {
                        
                        'fontSize' : '1rem',
                        'fontWeight' : '100'
                    
                    },
                    'BS' : {
                        
                        'fontSize' : '1rem',
                        'fontWeight' : '900'
                        
                    },
                    'Cum' : {
                        
                        'paddingLeft' : 5,
                        'fontWeight' : '600',
                        'fontSize' : '1rem',
                        'borderLeft' : self.borderBlack
                        
                    },
                    "Dean's" : {
                        
                        'paddingLeft' : 5,
                        'fontWeight' : '600',
                        'fontSize' : '1rem',
                        'borderLeft' : self.borderBlack
                        
                    },
                    'Awards' : {
                        
                        'fontWeight' : '300',
                        'fontSize' : '1.5rem',
                        'fontStyle' : 'italic'
                        
                    },
                    'Other' : {
                        
                        'paddingLeft' : 5,
                        'fontWeight' : '600',
                        'fontSize' : '1.1rem',
                        'borderLeft' : self.borderBlack
                        
                    },
                    'Kansas' : {
                        
                        'paddingLeft' : 5,
                        'marginBottom' : -5,
                        'fontWeight' : '900',
                        'fontSize' : '0.9rem',
                        'fontStyle' : 'italic',
                        'borderLeft' : self.borderBlack
                                                
                    },
                    'Packages' : {
                        
                        'fontWeight' : '500',
                        'fontSize' : '1.1rem',
                        'fontStyle' : 'italic',
                        'textDecoration' : 'underline'
                        
                    },
                    'Bachelor' : {
                        
                        'fontWeight' : '100',
                        'fontSize' : '0.9rem',
                        'fontStyle' : 'italic'
                        
                    },
                    'Languages' : {
                        
                        'fontWeight' : '500',
                        'fontSize' : '1.1rem',
                        'fontStyle' : 'italic',
                        'textDecoration' : 'underline'
                        
                    },
                    'University' : {
                        
                        'paddingLeft' : 5,
                        'fontWeight' : '900',
                        'fontSize' : '0.9rem',
                        'fontStyle' : 'italic',
                        'borderLeft' : self.borderBlack
                        
                    }
                    
                }[v.split(' ')[0] if (v.split(' ')[0] in styled) else False]
                
            }
            
        )