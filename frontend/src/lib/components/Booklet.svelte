<script lang="ts">
    import {currentPage, currentPageNumber, text, totalPages} from "../stores.ts";
    import Page from "./Page.svelte";
    let currentPageValue;
    let currentPageNumberValue;
    let totalPagesValue;
    let currentSnippet;

    currentPage.subscribe((value:any) => {
        if(value){
            currentPageValue=value
            currentSnippet = cleanSnippet(value?.snippet)
        }
    })

    currentPageNumber.subscribe(value => currentPageNumberValue=value)
    totalPages.subscribe(value => totalPagesValue=value)

    function cleanSnippet(snippet: string){
        if(!snippet){
            return ''
        }
        return snippet.replace(/^[^a-zA-Z]*/gi, '')
    }

    async function next(){
        if(currentPageValue.hasNext){
            currentPageNumber.update(n => n+1)
        }
    }
    async function previous(){
        if(currentPageValue.hasPrevious){
            currentPageNumber.update(n => n-1)
        }
    }
</script>
<div class="aspect-h-1 aspect-w-2 text-black">
    <div class="grid grid-cols-2 items-stretch">
        <div class="relative w-full group">
            <Page position="left" skew="skew-y-1"></Page>
            <Page position="left" skew="skew-y-2"></Page>
            <div on:click={previous}
                 class="absolute top-0 left-0 bg-amber-50 w-full rounded-l-2xl skew-y-3 {currentPageValue.hasPrevious?'hover:skew-y-[4deg] cursor-pointer':''} duration-200 border-r border-gray-400 shadow shadow-black/40 overflow-hidden  origin-top-right">
                <div class="aspect-h-1 aspect-w-1">
                    <div class="relative">
                        <div class="absolute w-full h-full">
                            <img src="{currentPageValue.image}" class="w-full ">
                        </div>
                        <div class="absolute shadow-booklet-l w-full h-full">
                        </div>
                    </div>
                </div>
            </div>
            <div on:click={previous} class="h-32 w-32 opacity-0 cursor-pointer text-lg bg-zinc-200/20  rounded-full absolute top-[35%] -left-8
                            flex justify-center items-center duration-1000 {currentPageValue.hasPrevious?'group-hover:opacity-100 group-hover:-left-16':''}">
                <svg width="30" height="58" class="-scale-x-100" viewBox="0 0 15 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path class="fill-current text-zinc-500/60" d="M1.99909 27.9964C1.53282 27.9973 1.08095 27.8349 0.721919 27.5374C0.51985 27.3699 0.352817 27.1641 0.230384 26.932C0.107952 26.6998 0.0325265 26.4457 0.00842816 26.1844C-0.0156701 25.923 0.0120325 25.6594 0.0899487 25.4088C0.167865 25.1581 0.294462 24.9253 0.462494 24.7236L9.40267 14.0274L0.781787 3.31113C0.616023 3.10701 0.492234 2.87214 0.417536 2.62002C0.342838 2.3679 0.318704 2.1035 0.346521 1.84203C0.374338 1.58055 0.453555 1.32715 0.579624 1.09639C0.705692 0.865624 0.876124 0.662052 1.08112 0.497372C1.2876 0.315702 1.52939 0.17867 1.79134 0.0948782C2.05328 0.0110859 2.32972 -0.0176577 2.6033 0.0104497C2.87688 0.0385572 3.14169 0.12291 3.38113 0.258213C3.62056 0.393517 3.82944 0.57685 3.99466 0.796708L13.6333 12.7702C13.9268 13.1272 14.0873 13.5751 14.0873 14.0373C14.0873 14.4996 13.9268 14.9475 13.6333 15.3045L3.65541 27.278C3.45522 27.5195 3.20092 27.7104 2.91314 27.8352C2.62536 27.96 2.3122 28.0152 1.99909 27.9964Z"/>
                </svg>
            </div>
        </div>
        <div class="relative w-full group">
            <Page position="right" skew="-skew-y-1"></Page>
            <Page position="right" skew="-skew-y-2"></Page>
            <div on:click={next} class="absolute top-0 left-0  w-full bg-amber-50 rounded-r-2xl -skew-y-3 {currentPageValue.hasNext?'hover:-skew-y-[4deg] cursor-pointer':''} duration-200 shadow shadow-black/40 origin-top-left">
                <div class="shadow-booklet-r">
                    <div class="aspect-h-1 aspect-w-1">
                        <div class="h-full flex flex-col">
                            <div class="flex-grow duration-200 p-12 max-w-xl mx-auto overflow-hidden text-clip overflow-hidden">
                                <p class="font-serif text-lg
                                        first-letter:font-king first-letter:text-7xl first-letter:float-left first-letter:mr-4 tracking-wide leading-7">
                                    {currentSnippet}
                                </p>
                            </div>
                            <div class="text-center py-8">
                                Page {currentPageNumberValue+1}/{totalPagesValue}
                            </div>

                        </div>

                    </div>
                </div>
                <div class="h-32 w-32 opacity-0 text-lg bg-zinc-200/20  rounded-full absolute top-[45%] -right-8
                            flex justify-center items-center duration-1000 {currentPageValue.hasNext?'group-hover:opacity-100 group-hover:-right-16':''}">
                    <svg width="30" height="58" viewBox="0 0 15 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path class="fill-current text-zinc-500/60" d="M1.99909 27.9964C1.53282 27.9973 1.08095 27.8349 0.721919 27.5374C0.51985 27.3699 0.352817 27.1641 0.230384 26.932C0.107952 26.6998 0.0325265 26.4457 0.00842816 26.1844C-0.0156701 25.923 0.0120325 25.6594 0.0899487 25.4088C0.167865 25.1581 0.294462 24.9253 0.462494 24.7236L9.40267 14.0274L0.781787 3.31113C0.616023 3.10701 0.492234 2.87214 0.417536 2.62002C0.342838 2.3679 0.318704 2.1035 0.346521 1.84203C0.374338 1.58055 0.453555 1.32715 0.579624 1.09639C0.705692 0.865624 0.876124 0.662052 1.08112 0.497372C1.2876 0.315702 1.52939 0.17867 1.79134 0.0948782C2.05328 0.0110859 2.32972 -0.0176577 2.6033 0.0104497C2.87688 0.0385572 3.14169 0.12291 3.38113 0.258213C3.62056 0.393517 3.82944 0.57685 3.99466 0.796708L13.6333 12.7702C13.9268 13.1272 14.0873 13.5751 14.0873 14.0373C14.0873 14.4996 13.9268 14.9475 13.6333 15.3045L3.65541 27.278C3.45522 27.5195 3.20092 27.7104 2.91314 27.8352C2.62536 27.96 2.3122 28.0152 1.99909 27.9964Z"/>
                    </svg>
                </div>
            </div>
        </div>

    </div>
</div>
