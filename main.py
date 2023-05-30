# Project Resume by Alex Arbuckle #


# import <
from dash import html
from lxRbckl import jsonLoad
import dash_bootstrap_components as dbc

from utility import (

    gDirectory,
    application,
    titleFunction,
    badgeFunction,
    spacerFunction,
    headerFunction,
    subjectFunction

)

# >


# global <
gData = jsonLoad(pFile = f'{gDirectory}/data.json')
gStyle = jsonLoad(pFile = f'{gDirectory}/style.json')

# >


application.layout = dbc.Container(

    fluid = True,
    style = dict(

        minHeight = '100vh',
        backgroundColor = gStyle['secondaryColor']

    ),
    children = dbc.Row(

        justify = 'center',
        children = [

            dbc.Col(

                width = 3,
                children = [

                    # cover <
                    # photo <
                    html.Div(

                        style = dict(

                            margin = '1vh 0px 0px 0px',
                            padding = '3vh 0px 3vh 0px',
                            backgroundColor = gStyle['tertiaryColor']

                        ),
                        children = html.Img(

                            src = gData['cover'],
                            className = 'col-12'

                        )

                    ),
                    html.Div(

                        style = dict(padding = '0px 0px 5% 0px'),
                        children = html.Img(

                            src = gData['photo'],
                            className = 'col-12'

                        )

                    ),

                    # >

                    # About Me <
                    # detail <
                    # spacer <
                    subjectFunction(

                        pStyle = gStyle,
                        pKey = 'Profile',
                        pData = gData['subject']

                    ),
                    *[

                        html.Div(

                            style = dict(padding = '0px 0px 5px 0px'),
                            children = [

                                html.H5(

                                    children = k,
                                    className = 'h6',
                                    style = dict(

                                        margin = '0px 0px -5px 0px',
                                        color = gStyle['primaryColor']

                                    )

                                ),
                                html.Small(

                                    children = v,
                                    style = dict(color = gStyle['primaryColor'])

                                )

                            ]

                        )

                    for k, v in gData['detail'].items()],
                    spacerFunction(

                        pPadding = '0.5px',
                        pMarginTop = '5px',
                        pBackgroundColor = gStyle['primaryColor']

                    )

                    # >

                ]

            ),

            dbc.Col(

                width = 3,
                children = [

                    # Pastimes <
                    subjectFunction(

                        pStyle = gStyle,
                        pKey = 'Pastimes',
                        pData = gData['subject'],
                        pPadding = '0px 0px 5% 0px'

                    ),

                    # >

                    # Skills <
                    html.Div(

                        style = dict(padding = '0px 0px 5% 0px'),
                        children = [

                            # spacer <
                            # title <
                            spacerFunction(

                                pPadding = '3px',
                                pBackgroundColor = gStyle['primaryColor']

                            ),
                            headerFunction(

                                pStyle = gStyle,
                                pChildren = 'Skills'

                            ),

                            # >

                            # iterate (language, topic) <
                            *[

                                html.Div(children = [

                                    # subtitle <
                                    # badge <
                                    # spacer <
                                    titleFunction(

                                        pStyle = gStyle,
                                        pChildren = {

                                            'library' : 'Libraries',
                                            'language' : 'Languages'

                                        }[i]

                                    ),
                                    badgeFunction(

                                        i = i,
                                        pStyle = gStyle

                                    ),
                                    spacerFunction(

                                        pPadding = '0.5px',
                                        pBackgroundColor = gStyle['primaryColor']

                                    )

                                    # >

                                ])

                            for i in ['language', 'library']],

                            # >

                        ]

                    ),

                    # >

                    # My Website <
                    html.Div(

                        style = dict(

                            padding = '1% 0px 1% 0px',
                            backgroundColor = gStyle['tertiaryColor']

                        ),
                        children = [

                            # spacer <
                            # title <
                            # QR <
                            spacerFunction(

                                pPadding = '3px',
                                pBackgroundColor = gStyle['primaryColor']

                            ),
                            headerFunction(

                                pStyle = gStyle,
                                pChildren = 'My Website'

                            ),
                            html.Img(

                                src = gData['QR'],
                                className = 'col-5 text-center'

                            ),
                            spacerFunction(

                                pPadding = '0.5px',
                                pBackgroundColor = gStyle['primaryColor']

                            )

                            # >

                        ]

                    )

                    # >

                ]

            ),

            dbc.Col(

                width = 3,
                children = [

                    # Experience <
                    # Education <
                    # Awards <
                    subjectFunction(

                        pStyle = gStyle,
                        pKey = 'Experience',
                        pData = gData['subject'],
                        pPadding = '0px 0px 5% 0px'

                    ),
                    subjectFunction(

                        pStyle = gStyle,
                        pKey = 'Education',
                        pData = gData['subject'],
                        pPadding = '1% 0px 1% 0px',
                        pBackgroundColor = gStyle['tertiaryColor']

                    ),
                    subjectFunction(

                        pStyle = gStyle,
                        pKey = 'Awards',
                        pData = gData['subject'],
                        pPadding = '5% 0px 0px 0px'

                    )

                    # >

                ]

            )

        ]

    )

)


# main <
if (__name__ == '__main__'): application.run_server()

# >