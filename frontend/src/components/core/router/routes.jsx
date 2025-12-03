import { lazy } from "react"
import { createBrowserRouter } from "react-router-dom"
import App from '../../../App'

const Home = lazy(() => import('../../../view/home.jsx'))
const Simple = lazy(() => import('../../../view/simple.jsx'))
const Memory = lazy(() => import('../../../view/memory.jsx'))
const Sequential = lazy(() => import('../../../view/sequential.jsx'))
const CompareSen = lazy(() => import('../../../view/rag-basics/compareSen.jsx'))
const TransformSen = lazy(() => import('../../../view/rag-basics/transformSen.jsx'))
const Recommandation = lazy(() => import('../../../view/rag-basics/recommandation.jsx'))
const PdfSearch = lazy(()=> import('../../../view/rag-basics/pdfSearch.jsx'))



const routes = [

    {
        path: '/',
        element: <App />,
        children: [
            { path: "", element: <Home /> },
            { path: "simple", element: <Simple /> },
            { path: "sequential", element: <Sequential /> },
            { path: "memory", element: <Memory /> },
            { path: "rag-basics/compareSen", element: <CompareSen /> },
            { path: "rag-basics/transformSen", element: <TransformSen /> },
            { path: "rag-basics/recommandation", element: <Recommandation /> },
            { path: "rag-basics/pdfSearch", element: <PdfSearch /> },
        ]


    },

];

export const router = createBrowserRouter(routes) 