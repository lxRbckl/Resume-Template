# Project Resume by Alex Arbuckle #

# rgb(52, 73, 95)
#
#

# import <
from dash import html
from lxRbckl import jsonLoad
import dash_bootstrap_components as dbc

from resource import spacerFunction, headerFunction, titleFunction
from resource import application, gDirectory, subjectFunction, badgeFunction

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
                            padding = '2vh 0px 2vh 0px',
                            backgroundColor = gStyle['primaryColor']

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

                        pKey = 'Pastimes',
                        pData = gData['subject'],
                        pPadding = '0px 0px 5% 0px'

                    ),

                    # >

                    # Education <
                    subjectFunction(

                        pKey = 'Education',
                        pData = gData['subject'],
                        pPadding = '1% 0px 1% 0px',
                        pColor = gStyle['secondaryColor'],
                        pBackgroundColor = gStyle['primaryColor']

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

                                        pChildren = {

                                            'library' : 'Libraries',
                                            'language' : 'Languages'

                                        }[i]

                                    ),
                                    badgeFunction(

                                        i = i,

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

                    )

                    # >

                ]

            ),

            dbc.Col(

                width = 3,
                children = [

                    # Awards <
                    # Experience <
                    subjectFunction(

                        pKey = 'Awards',
                        pData = gData['subject'],
                        pPadding = '0px 0px 5% 0px'

                    ),
                    subjectFunction(

                        pKey = 'Experience',
                        pData = gData['subject'],
                        pPadding = '0px 0px 5% 0px'


                    )

                    # >

                ]

            )

        ]

    )

)


# main <
if (__name__ == '__main__'): application.run_server(debug = True)

# >
