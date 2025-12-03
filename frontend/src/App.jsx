import { Suspense } from 'react'
import { Outlet } from 'react-router-dom'
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "./components/core/appSidebar"


function App() {
  return (
    <SidebarProvider>
      <AppSidebar />
        <div className="p-4">
          <SidebarTrigger />
        </div>
     <div className="flex-1 pt-4">
          <Outlet />
        </div>
    </SidebarProvider>
  )
}

export default App