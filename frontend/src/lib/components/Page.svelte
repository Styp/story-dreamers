<script>
    import {currentPage, currentPageNumber, text, totalPages} from "../stores.ts";
    import {nextPage, previousPage} from "../api.ts";
    import Button from "./Button.svelte";

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

    async function reset(){
        text.set('')
        currentPage.set(null)
        currentPageNumber.set(1)
    }
</script>

<div class="grid grid-cols-12 gap-8 items-center ">
    <div class="col-span-12 pt-12">
        <div class="aspect-h-1 aspect-w-2">
            <div class="grid grid-cols-2 items-stretch">
                <div class="relative w-full">
                    <div class="absolute top-0 left-0 bg-amber-50 w-full rounded-l-2xl skew-y-1 shadow shadow-black/40 overflow-hidden origin-top-right">
                        <div class="aspect-h-1 aspect-w-1"></div>
                    </div>
                    <div class="absolute top-0 left-0 bg-amber-50 w-full rounded-l-2xl skew-y-2 shadow shadow-black/40 overflow-hidden origin-top-right">
                        <div class="aspect-h-1 aspect-w-1"></div>
                    </div>
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
                    <div class="absolute top-0 left-0 bg-amber-50 w-full rounded-r-2xl -skew-y-1 shadow shadow-black/40 overflow-hidden origin-top-left">
                        <div class="aspect-h-1 aspect-w-1"></div>
                    </div>
                    <div class="absolute top-0 left-0 bg-amber-50 w-full rounded-r-2xl -skew-y-2 shadow shadow-black/40 overflow-hidden origin-top-left">
                        <div class="aspect-h-1 aspect-w-1"></div>
                    </div>
                    <div on:click={next} class="absolute top-0 left-0  w-full bg-amber-50 rounded-r-2xl -skew-y-3 {currentPageValue.next?'hover:-skew-y-[4deg] cursor-pointer':''} duration-200 shadow shadow-black/40 origin-top-left">
                        <div class="aspect-h-1 aspect-w-1 shadow-booklet-r">
                            <div class="skew-y-1 {currentPageValue.next?'hover:skew-y-2':''} duration-200 p-12">
                                {currentPageValue.snippet}
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
    <div class="col-span-6 col-start-4 grid grid-cols-9">
        <div class="col-span-3 flex justify-end">
            {#if currentPageValue.previous}
                <Button on:click={previous}>Previous</Button>
            {/if}
        </div>
        <div class="col-span-3 flex justify-center">
            Page {currentPageNumberValue}/{totalPagesValue}
        </div>
        <div class="col-span-3 flex justify-start">
            {#if currentPageValue.next}
                <Button on:click={next}>Next</Button>
            {/if}
        </div>
    </div>

    <div class="col-span-3 flex justify-end">
        <Button on:click={reset}>Read another story</Button>
    </div>
</div>