import {currentPageNumber} from "./stores";
import {get} from "svelte/store";

const host = 'http://127.0.0.1:8080'
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
    return fetch(`${host}/${textEndpoint}`, {
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
    return fetch(`${host}/${imageEndpoint}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            prompt: prompt
        })
    }).then(
            response => response.json()
        )
}