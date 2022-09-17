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
        currentPage.set(await nextPage(currentPageValue))
        currentPageNumber.update(n => n+1)
    }
    async function previous(){
        currentPage.set(await previousPage(currentPageValue))
        currentPageNumber.update(n => n-1)
    }

    async function reset(){
        text.set('')
        currentPage.set(null)
        currentPageNumber.set(1)
    }
</script>

<div class="grid grid-cols-12 gap-8 items-center ">
    <div class="col-span-8">
        <img src="{currentPageValue.image}">
    </div>
    <div class="col-span-4">
        {currentPageValue.snippet}
    </div>
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
    <div class="col-span-3 flex justify-end">
        <Button on:click={reset}>Reset</Button>
    </div>
</div>