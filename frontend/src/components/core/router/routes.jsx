import { lazy } from "react"
import { createBrowserRouter } from "react-router-dom"
import App from '../../../App'

const Home = lazy(()=> import('../../../view/home.jsx'))


const routes = [

    {
        path:'/',
        element: <App />,
        children: [

            {path: '', element: <Home />},
          //  {path: 'project', element: <Project /> },  
          // {path: 'aboutMe', element: <AboutMe />},


        ],

    },

];

export const router = createBrowserRouter(routes) 