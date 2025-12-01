import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupLabel,
  SidebarGroupContent,
  SidebarMenu,
  SidebarMenuItem,
  SidebarMenuButton
} from "@/components/ui/sidebar"
import { Calendar, Home, Inbox, Search, Settings } from "lucide-react"

export function AppSidebar(){

const items = [
  {
    title: "Normal",
    url: "#",
  },
  {
    title: "Chain",
    url: "#",
  },
  {
    title: "Sequential",
    url: "#",
  },
  {
    title: "Memory",
    url: "#",
  },
  {
    title: "Settings",
    url: "#",
  },
]

return (

    <Sidebar>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Application</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {items.map((item) => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton asChild>
                    <a href={item.url}>
                      <span>{item.title}</span>
                    </a>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
)

}