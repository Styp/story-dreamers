<script>
    import {currentPage, currentPageNumber, text, totalPages} from "../stores.ts";
    import {nextPage, previousPage} from "../api.ts";
    import Button from "./Button.svelte";
    import Booklet from "./Booklet.svelte";

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
        <Booklet></Booklet>
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