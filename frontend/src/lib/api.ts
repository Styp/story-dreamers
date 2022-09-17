
const host = 'http://127.0.0.1:8000'
const endpoint = 'magic'

export interface ServerResponse{
    firstPage: string
    totalPages: number
}

export interface ServerPage {
    snippet: string
    image: string
    next?: string|null
    previous?: string|null
}


export interface ProcessedTextItem{
    snippet: string
    processedText: string
}

export interface ProcessedTextResponse{
    data: ProcessedTextItem[]
}
export interface ImagePage {
    image: string
}


export async function send_text_to_server(text: string): Promise<ServerResponse>{
    return fetch(`${host}/${endpoint}`, {
        method: 'POST',
        body: JSON.stringify({
            text: text
        })
    }).then(
        response => response.json()
    )
}

export async function nextPage(page: ServerPage): Promise<ServerPage>{
    if(page.next){
        return await get_page(page.next)
    }
    return null
}

export async function previousPage(page: ServerPage): Promise<ServerPage>{
    if(page.previous){
        return await get_page(page.previous)
    }
    return null
}

export async function get_page(url): Promise<ServerPage>{
    return fetch(url)
        .then(
            response => response.json()
        )
}