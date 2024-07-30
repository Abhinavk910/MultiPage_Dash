from dash import Dash, html, Input, Output, \
    dcc, clientside_callback, ALL, State, register_page
import dash_bootstrap_components as dbc
from dash.html import Div, Section, H1, H2, H3, Main, P, Img, Footer, A

register_page(__name__, path='/skewed1')

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
    className='font-sans overflow-x-hidden',
    style={'padding': 0, 'margin': 0, 'boxSizing': 'border-box'},
    children=[
        Section(
            className="h-screen min-h-[35em] relative bg-[url('/assets/website/image1.jpg')] bg-center bg-no-repeat bg-cover -z-2",
            children=[
                Div(
                    className='mx-auto max-w-[1200px] p-8 h-full relative flex justify-center items-center',
                    children=[
                        H1(
                            'Skewed Design',
                            className='text-[3em] text-[clamp(2em,5vw,6em)] text-white'
                        ),
                        html.Div(
                            className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-black opacity-60  w-screen h-full -z-1"
                        ),
                        # Div(
                        #     className='absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-black bg-opacity-70 w-screen h-full -z-10'
                        # )
                    ]
                )
            ]
        ),
        Main(
            Div(
                className='container',
                children=[
                    H2(
                        'Additional Content'
                    ),
                    P(
                        """
                        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                        """
                    ),
                    P(
                        """
                        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                        """
                    ),
                    P(
                        """
                        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                        """
                    ),
                    Img(
                        src="/assets/website/image1.jpg",
                    ),
                    P(
                        """
                        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                        """
                    ),
                    
                ]
            )
        ),
        Footer(
            children=[
                Div(
                    className='container',
                    children=[
                        Div(
                            children=[
                                H3(
                                    'Brand'
                                ),
                                P(
                                    """
                                    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                                    """
                                ),
                            ]
                        ),
                        Div(
                            className='link',
                            children=[
                                A(
                                    'Home',
                                    href='#'
                                ),
                                A(
                                    'About',
                                    href='#'
                                ),
                                A(
                                    'Contract',
                                    href='#'
                                ),
                                A(
                                    'Blog',
                                    href='#'
                                ),
                            ]
                        ),
                        Div(
                            className='link',
                            children=[
                                A(
                                    'Facebook',
                                    href='#'
                                ),
                                A(
                                    'Instagram',
                                    href='#'
                                ),
                                A(
                                    'Tiktok',
                                    href='#'
                                ),
                                A(
                                    'Youtube',
                                    href='#'
                                ),
                            ]
                        ),
                        Div(
                            className='link',
                            children=[
                                A(
                                    'Additional Link',
                                    href='#'
                                ),
                                A(
                                    'One More',
                                    href='#'
                                ),
                                A(
                                    'And another',
                                    href='#'
                                ),
                            ]
                        )
                    ]
                ),
                Div(
                    className='copyright',
                    children=[
                        P(
                            '@ Copyright AK.com'
                        )
                    ]
                )
            ]
        )
        
        
        
    ]
)






# clientside_callback(
#     """
#     function (url) {
#         console.log(url)
#         return url;
#     }
#     """,
#     Output('heading', 'children'),
#     Input('url', 'pathname')
# )