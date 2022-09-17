import {currentPageNumber} from "./stores";
import {get} from "svelte/store";

const host = '' // 'http://127.0.0.1:8080'
const endpoint = 'fake-responses/text-processing.json'
const imageEndpoint = 'fake-responses/001.json'

export interface BookletPage {
    snippet: string
    image: string
    hasNext: boolean
    hasPrevious: boolean
}


export interface ProcessedTextItem{
    snippet: string
    processedText: string
}

export interface ProcessedTextResponse{
    data: ProcessedTextItem[]
}
export interface ImagePrompt {
    image: string
}


export async function send_text_to_server(text: string): Promise<ProcessedTextResponse>{
    return fetch(`${host}/${endpoint}`, {
        method: 'POST',
        body: JSON.stringify({
            text: text
        })
    }).then(
        response => response.json()
    )
}

export async function get_image(prompt: string): Promise<ImagePrompt>{
    const fakeEndpoint = `fake-responses/00${get(currentPageNumber)+1}.json`
    return fetch(`${host}/${fakeEndpoint}`, {
        method: 'POST',
        body: JSON.stringify({
            prompt: prompt
        })
    }).then(
            response => response.json()
        )
}