import { Suspense } from 'react'
import { Outlet } from 'react-router-dom'
import './App.css'
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "./components/core/appSidebar"


function App() {
  return (
    <>
      <SidebarProvider>
        <AppSidebar />
        <main>
          <SidebarTrigger />
          <Outlet />
        </main>
      </SidebarProvider>
    </>
  )
}

export default App