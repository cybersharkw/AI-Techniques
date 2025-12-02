import { lazy } from "react"
import { createBrowserRouter } from "react-router-dom"
import App from '../../../App'

const Home = lazy(()=> import('../../../view/home.jsx'))
const Simple = lazy(()=> import('../../../view/simple.jsx'))
const Memory = lazy(()=> import('../../../view/memory.jsx'))
const Sequential = lazy(()=> import('../../../view/sequential.jsx'))

const routes = [

    {
        path:'/',
        element: <App />,
        children: [

            {path: '', element: <Home />},
            {path: '/simple', element: <Simple /> },  
            {path: '/sequential', element: <Sequential />},
            {path: '/memory', element: <Memory />},


        ],

    },

];

export const router = createBrowserRouter(routes) 