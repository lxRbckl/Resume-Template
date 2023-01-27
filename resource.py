# import <
from os import path
from dash import Dash, html
from lxRbckl import requestsGet
import dash_bootstrap_components as dbc

# >


# global <
gDataLink = 'https://raw.githubusercontent.com/lxRbckl/Project-Heimir/main/data.json'

gDirectory = '/'.join(path.realpath(__file__).split('/')[:-1])
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

        pStyle: dict,
        pChildren: str

):
    '''  '''

    return html.H2(

        children = pChildren,
        className = 'display-5',
        style = dict(

            margin = '-7px 0px 3px 0px',
            color = pStyle['primaryColor']

        )

    )


def titleFunction(

        pStyle: dict,
        pChildren: str

):
    '''  '''

    return html.H3(

        children = pChildren,
        style = dict(

            margin = '0px 0px -10px 0px',
            color = pStyle['primaryColor']

        )

    )


def subtitleFunction(

        i: str,
        pKey: str,
        pData: dict,
        pStyle: dict,
        isBold: bool = False,
        pValue: str = 'subtitleA'

):
    '''  '''

    return html.H2(

        className = 'lead',
        children = pData[pKey][i][pValue],
        style = dict(

            fontSize = 15,
            margin = '8px 0px -8px 0px',
            color = pStyle['primaryColor'],
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
        pStyle: dict

):
    '''  '''

    return [

        html.P(

            children = i,
            style = dict(

                margin = '15px 0px 0px 0px',
                color = pStyle['primaryColor']

            )

        )

    for i in pData[pKey][i]['text']]


def badgeFunction(

        i: str,
        pStyle: dict,
        pData: dict = requestsGet(pLink = gDataLink)

):
    '''  '''

    return html.Div(

        style = dict(padding = '10px 0px 0px 0px'),
        children = [

            dbc.Badge(

                children = i.replace('-', ' '),
                color = pStyle['primaryColor'],
                style = dict(

                    padding = 6,
                    margin = '0px 1px 0px 1px',
                    color = pStyle['secondaryColor']

                )

            )

        for i in pData[i]])


def subjectFunction(

        pKey: str,
        pData: dict,
        pStyle: dict,
        pPadding: str = None,
        pSubtitle: str = None,
        pChildren: list = None,
        pBackgroundColor: str = None

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
                pBackgroundColor = pStyle['primaryColor']

            ),
            headerFunction(

                pStyle = pStyle,
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
                        pStyle = pStyle

                    ),
                    subtitleFunction(

                        i = i,
                        pKey = pKey,
                        pData = pData,
                        isBold = True,
                        pStyle = pStyle,
                        pValue = 'subtitleB'

                    ),
                    subtitleFunction(

                        i = i,
                        pKey = pKey,
                        pData = pData,
                        pStyle = pStyle

                    ),

                    # >

                    # text <
                    # spacer <
                    *textFunction(

                        i = i,
                        pKey = pKey,
                        pData = pData,
                        pStyle = pStyle

                    ),
                    spacerFunction(

                        pPadding = '0.5px',
                        pBackgroundColor = pStyle['primaryColor']

                    )

                    # >

                ]) if (pData[pKey][i]['display']) else None

            for i in pData[pKey].keys()]

            # >

        ]

    )
