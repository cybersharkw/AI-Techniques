import { use, useState } from "react"
import {Input} from "../ui/input"
import {Button} from "../ui/button"
import { callBackend } from "@/api/callApi.js"

export function Chat(api) {

    const [messages, setMessages] = useState([])
    const [input, setInput] = useState("")

    async function handleSubmit(e) {
    e.preventDefault();

    if (!input.trim()) return

    //Add user Messages
    setMessages(prev => [...prev, { role: "user", text: input }])

    const currentInput = input
    //empty Input
    setInput("")

    try {
        console.log(api.api)
        const result = await callBackend(api.api, {
            query: currentInput
        })

        //Add response
        setMessages(prev => [...prev, { role: "assistant", text: result.result }])

    } catch (error){
        console.error(error)
    }
}


    return (

        <div className="w-full max-w-lg mx-auto space-y-4">

            {/* Chat Window */}
            <section className="border h-200 p-4 overflow-y-auto rounded-lg bg-white shadow">
                {messages.map((m, i) => (
                    <div
                        key={i}
                        className={`mb-2 p-2 rounded-lg ${m.role === "user"
                                ? "bg-blue-100 text-right"
                                : "bg-gray-100 text-left"
                            }`}
                    >
                        {m.text}
                    </div>
                ))}

            </section>

            <section>
                <form className="flex gap-2" onSubmit={handleSubmit}>
                    <Input placeholder="Ask something"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                    />

                    <Button type="Submit"></Button>
                </form>


            </section>

        </div>
    )
}