import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupLabel,
  SidebarGroupContent,
  SidebarMenu,
  SidebarMenuItem,
  SidebarMenuButton,
  SidebarHeader,
} from "@/components/ui/sidebar"
import { ChevronDown} from "lucide-react"

import {
  Collapsible,
  CollapsibleTrigger,
  CollapsibleContent
} from "@/components/ui/collapsible"


export function AppSidebar() {

  const items = [
    {
      title: "Simple",
      url: "/simple",
      section: 1
    },
    {
      title: "Sequential",
      url: "/sequential",
      section: 1
    },
    {
      title: "Memory",
      url: "/memory",
      section: 1
    },
    {
      title: "Settings",
      url: "#",
    },
  ]

  return (

    <Sidebar>
      <SidebarHeader>AI-techniques</SidebarHeader>
      <SidebarContent>

        {/* Sprint one*/}
        <Collapsible defaultOpen className="group/collapsible">
          <SidebarGroup>
            <SidebarGroupLabel>
              <CollapsibleTrigger>Langchain </CollapsibleTrigger><ChevronDown className="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-180" /></SidebarGroupLabel>
            <CollapsibleContent>
              <SidebarGroupContent>
                <SidebarMenu>
                  {items.filter(item => item.section === 1)
                    .map(item => (
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
            </CollapsibleContent>
          </SidebarGroup>
        </Collapsible>

        {/* Sprint two*/}
         <Collapsible defaultOpen className="group/collapsible">
          <SidebarGroup>
            <SidebarGroupLabel>
              <CollapsibleTrigger>Langchain </CollapsibleTrigger><ChevronDown className="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-180" /></SidebarGroupLabel>
            <CollapsibleContent>
              <SidebarGroupContent>
                <SidebarMenu>
                  {items.filter(item => item.section === 2)
                    .map(item => (
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
            </CollapsibleContent>
          </SidebarGroup>
        </Collapsible>

      </SidebarContent>
    </Sidebar>
  )

}