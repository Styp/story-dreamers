import {currentPageNumber, loading, promptCache} from "./stores";
import {get} from "svelte/store";

const host = 'http://34.91.232.232:8000'
const textEndpoint = 'promptsFromText' // 'promptsFromText'
const imageEndpoint = 'base64FromPrompt' // 'base64FromPrompt'

export interface BookletPage {
    snippet: string
    image: string
    hasNext: boolean
    hasPrevious: boolean
}


export interface ProcessedTextItem{
    snippet: string
    prompt: string
}

export interface ImagePrompt {
    image: string
}


export async function send_text_to_server(text: string): Promise<ProcessedTextItem[]>{
    return await fetch(`${host}/${textEndpoint}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: text
        })
    }).then(
        response => response.json()
    )
}

export async function get_image(prompt: string): Promise<ImagePrompt>{
    const cacheValue = get(promptCache)
    if(cacheValue[prompt]){
        console.log('cache hit')
        setTimeout(() => loading.set(false),5000)
        return cacheValue[prompt]
    }
    else{
        console.log('cache miss')
    }
    return await fetch(`${host}/${imageEndpoint}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            prompt: prompt
        })
    })
        .then(
            response => response.json()
        )
        .then(
            response => {
                promptCache.update(cache => {cache[prompt] = response; return cache});
                setTimeout(() => loading.set(false),5000)
                return response}
        )
}