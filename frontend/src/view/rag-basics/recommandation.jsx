import {Chat} from '../../components/core/chat'

export default function Recommandation(){

    return(

        <div>
            <Chat api='/api/langchain/memory'/>
        </div>
    )
}