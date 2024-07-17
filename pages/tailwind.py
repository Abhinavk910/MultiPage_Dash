from dash import Dash, html, Input, Output, \
    dcc, clientside_callback, ALL, State, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path='/tailwindnavbar')
#if you creating new dash just replace above with this 
# app = Dash(
#     __name__, 
#     external_scripts=['https://cdn.tailwindcss.com'],
#     external_stylesheets=[dbc.icons.BOOTSTRAP]
# )


def sidebar_icon(id: str, icon: str, href: str, tooltip: str):

    return dcc.Link(
        className="""
            group
            flex items-center justify-center no-underline
            h-12 w-12 mt-2 mb-2 mx-auto  
            bg-gray-300 hover:bg-green-600 
            text-green-500 hover:text-white 
            rounded-3xl hover:rounded-xl
            transition-all duration-300 ease-linear
            cursor-pointer shadow-lg
            """,
        href=href,
        id={'type': 'sidebar-icon', 'index': str(id)},
        children=[
            html.I(className="bi bi-" + icon, style={'fontSize':'24px'}),
            html.Span(
                className=""" 
                    absolute w-auto p-2 m-2 min-w-max left-14 
                    rounded-md shadow-md
                    text-white bg-gray-900 
                    text-xs font-bold 
                    transition-all duration-100 scale-0 
                    origin-left group-hover:scale-100""",
                children=[
                    tooltip
                ]
            )
        ]
    )

#replace layout with app.layout
layout = html.Div(
    className='flex',
    children=[
        dcc.Location(id='url', refresh='callback-nav'),
        html.Nav(
            className='fixed top-0 left-0 h-screen w-16\
                    flex flex-col bg-gray-100 dark:bg-gray-900 shadow-lg',
            children=[
                # Navigation items will be added here
                sidebar_icon(1, 'gem', '/home', 'Home'),
                html.Hr(className="bg-gray-200 \
                        border border-gray-200 rounded-full"),
                sidebar_icon(2, 'plus-lg', '/add', 'Add'),
                sidebar_icon(3, 'cart-check-fill', '/check', 'Check'),
                sidebar_icon(4, 'fan', '/run', 'Run'),
                html.Hr(className="bg-gray-200 \
                        border border-gray-200 rounded-full"),
                sidebar_icon(5, 'gear-fill', '/setting', 'Setting'),
            ]
        ),
        html.Main(
            className='flex-1',
            children=[
                html.Div(
                    className="""flex flex-row items-center justify-evenly bg-gray-300 dark:bg-gray-700 bg-opacity-90 
                                w-full h-16 m-0  pl-20 shadow-lg""",
                    children=[
                        html.H5('', id='heading', className="""
                                text-xl text-gray-500 tracking-wider font-semibold text-opacity-80 
                                mr-auto ml-2 my-auto transition duration-300 ease-in-out
                            """
                        ),                
                    ]
                ),
                html.Div(
                    className='min-h-screen bg-gray-100 flex flex-col ',
                    children=[
                        html.Main(
                            className='flex-grow p-4 pl-20',
                            children=[]
                        ),
                        html.Footer(
                            className='bg-gray-800 text-white p-4 text-center',
                            children='© 2024 AK.com'
                        )
                    ]
                )
            ]
        )
    ]
)

clientside_callback(
    """
    function (url) {
        console.log(url)
        return url;
    }
    """,
    Output('heading', 'children'),
    Input('url', 'pathname')
)