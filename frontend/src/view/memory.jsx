import {Chat} from '../components/core/chat'

export default function Memory(){

    return(

        <div>
            <Chat api='/api/langchain/memory'/>
        </div>
    )
}