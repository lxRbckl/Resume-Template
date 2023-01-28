# import <
from os import path
from dash import Dash, html
import dash_bootstrap_components as dbc
from lxRbckl import requestsGet, jsonLoad

# >


# global <
gDataLink = 'https://raw.githubusercontent.com/lxRbckl/Project-Heimir/main/data.json'
gDirectory = '/'.join(path.realpath(__file__).split('/')[:-1])
gStyle = jsonLoad(pFile = f'{gDirectory}/style.json')
gData = jsonLoad(pFile = f'{gDirectory}/data.json') # <
application = Dash(

    name = 'Resume',
    title = 'Resume',
    suppress_callback_exceptions = True,
    external_stylesheets = [

        dbc.themes.GRID,
        dbc.themes.BOOTSTRAP

    ]

)

# >


def spacerFunction(

        pPadding: str,
        pBackgroundColor: dict,
        pMarginTop: str = '1vh',
        pMarginBottom: str = '1vh'

):
    '''  '''

    return html.Div(style = dict(

        padding = pPadding,
        marginTop = pMarginTop,
        marginBottom = pMarginBottom,
        backgroundColor = pBackgroundColor

    ))


def headerFunction(

        pChildren: str,
        pColor: str = gStyle['primaryColor']

):
    '''  '''

    return html.H2(

        children = pChildren,
        className = 'display-5',
        style = dict(

            color = pColor,
            margin = '-7px 0px 3px 0px'

        )

    )


def titleFunction(

        pChildren: str,
        pColor: str = gStyle['primaryColor']

):
    '''  '''

    return html.H3(

        children = pChildren,
        style = dict(

            color = pColor,
            margin = '0px 0px -10px 0px'

        )

    )


def subtitleFunction(

        i: str,
        pKey: str,
        pData: dict,
        isBold: bool = False,
        pValue: str = 'subtitleA',
        pColor: str = gStyle['primaryColor']

):
    '''  '''

    return html.H2(

        className = 'lead',
        children = pData[pKey][i][pValue],
        style = dict(

            fontSize = 15,
            color = pColor,
            margin = '8px 0px -8px 0px',
            fontWeight = {

                True : 'bolder',
                False : 'normal'

            }[isBold]

        )

    ) if (pData[pKey][i][pValue]) else None


def textFunction(

        i: str,
        pKey: str,
        pData: dict,
        pColor: str = gStyle['primaryColor']

):
    '''  '''

    return [

        html.P(

            children = i,
            style = dict(

                color = pColor,
                margin = '15px 0px 0px 0px'

            )

        )

    for i in pData[pKey][i]['text']]


def badgeFunction(

        i: str,
        pColor: str = gStyle['primaryColor'],
        pData: dict = requestsGet(pLink = gDataLink)

):
    '''  '''

    return html.Div(

        style = dict(padding = '10px 0px 0px 0px'),
        children = [

            dbc.Badge(

                color = gStyle['primaryColor'],
                children = i.replace('-', ' '),
                style = dict(

                    padding = 6,
                    margin = '0px 1px 0px 1px',
                    color = gStyle['secondaryColor']

                )

            )

        for i in pData[i]])


def subjectFunction(

        pKey: str,
        pData: dict,
        pPadding: str = None,
        pSubtitle: str = None,
        pChildren: list = None,
        pBackgroundColor: str = None,
        pColor: str = gStyle['primaryColor']

):
    '''  '''

    return html.Div(

        style = dict(

            padding = pPadding,
            backgroundColor = pBackgroundColor

        ),
        children = [

            # spacer <
            # title <
            spacerFunction(

                pPadding = '3px',
                pBackgroundColor = pColor

            ),
            headerFunction(

                pColor = pColor,
                pChildren = pKey

            ),

            # >

            # iterate (content) <
            *[

                html.Div(children = [

                    # title <
                    # subtitle <
                    # subtitle <
                    titleFunction(

                        pChildren = i,
                        pColor = pColor

                    ),
                    subtitleFunction(

                        i = i,
                        pKey = pKey,
                        pData = pData,
                        isBold = True,
                        pColor = pColor,
                        pValue = 'subtitleB'

                    ),
                    subtitleFunction(

                        i = i,
                        pKey = pKey,
                        pData = pData,
                        pColor = pColor

                    ),

                    # >

                    # text <
                    # spacer <
                    *textFunction(

                        i = i,
                        pKey = pKey,
                        pData = pData,
                        pColor = pColor

                    ),
                    spacerFunction(

                        pPadding = '0.5px',
                        pBackgroundColor = pColor

                    )

                    # >

                ]) if (pData[pKey][i]['display']) else None

            for i in pData[pKey].keys()]

            # >

        ]

    )
