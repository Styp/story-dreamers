## Run Frontend
```
npm install
npm run dev
```

## API Thoughts:
* return base64 encoded image is probably easier to handle on the backend instead of sending an url
* Alternative: To keep the backend mostly stateless, return the results of the text processing as an 
  array of strings and let the client handle the state of requesting each image/sentence in order.


```Typescript

interface ServerResponse{
    firstPage: string  // url to first page
    totalPages: number
}

interface TextPage{
    snippet: string //text snippet
    image: string // maybe an array of strings? string[]
    next?: string|null // url to next page
    previous?: string|null // url to previous page
}
```

Alternative:
```Typescript
interface TextProcessingResponse{
    data: {
        snippet: string // Text Snippet
        processedText: string // Processed Text to pass to the image api
    }[]
}

interface ImagePage{
    image: string // maybe an array of strings? string[]
}
```