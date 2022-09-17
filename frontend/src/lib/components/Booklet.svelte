<script>
    import {currentPage, currentPageNumber, text, totalPages} from "../stores.ts";
    import {nextPage, previousPage} from "../api.ts";
    import Page from "./Page.svelte";

    let currentPageValue;
    let currentPageNumberValue;
    let totalPagesValue;

    currentPage.subscribe(value => currentPageValue=value)
    currentPageNumber.subscribe(value => currentPageNumberValue=value)
    totalPages.subscribe(value => totalPagesValue=value)

    async function next(){
        if(currentPageValue.next){
            currentPage.set(await nextPage(currentPageValue))
            currentPageNumber.update(n => n+1)
        }
    }
    async function previous(){
        if(currentPageValue.previous){
            currentPage.set(await previousPage(currentPageValue))
            currentPageNumber.update(n => n-1)
        }
    }
</script>
<div class="aspect-h-1 aspect-w-2">
    <div class="grid grid-cols-2 items-stretch">
        <div class="relative w-full">
            <Page position="left" skew="skew-y-1"></Page>
            <Page position="left" skew="skew-y-2"></Page>
            <div on:click={previous}
                 class="absolute top-0 left-0 bg-amber-50 w-full rounded-l-2xl skew-y-3 {currentPageValue.previous?'hover:skew-y-[4deg] cursor-pointer':''} duration-200 border-r border-gray-400 shadow shadow-black/40 overflow-hidden  origin-top-right">
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
        </div>
        <div class="relative w-full">
            <Page position="right" skew="skew-y-1"></Page>
            <Page position="right" skew="skew-y-2"></Page>
            <div on:click={next} class="absolute top-0 left-0  w-full bg-amber-50 rounded-r-2xl -skew-y-3 {currentPageValue.next?'hover:-skew-y-[4deg] cursor-pointer':''} duration-200 shadow shadow-black/40 origin-top-left">
                <div class="aspect-h-1 aspect-w-1 shadow-booklet-r">
                    <div class=" duration-200 p-12 max-w-xl mx-auto">
                        <p class="font-serif text-lg first-letter:font-king first-letter:text-7xl first-letter:float-left first-letter:mr-4 tracking-wide leading-7">
                            {currentPageValue.snippet}
                        </p>
                    </div>
                </div>
            </div>
        </div>

    </div>
</div>
