<script>
    import {currentPage, currentPageNumber, reset_story, text, totalPages} from "../stores.ts";
    import Button from "./Button.svelte";
    import Booklet from "./Booklet.svelte";

    let currentPageValue;
    let currentPageNumberValue;
    let totalPagesValue;

    currentPage.subscribe(value => currentPageValue=value)
    currentPageNumber.subscribe(value => currentPageNumberValue=value)
    totalPages.subscribe(value => totalPagesValue=value)

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

    async function reset(){
        reset_story()
    }
</script>

<div class="grid grid-cols-12 gap-8 items-center ">
    <div class="col-span-12 pt-12">
        <Booklet></Booklet>
    </div>
    <div class="col-span-6 col-start-4 grid grid-cols-9">
        <div class="col-span-3 flex justify-end">
            {#if currentPageValue.hasPrevious}
                <Button on:click={previous}>Previous</Button>
            {/if}
        </div>
        <div class="col-span-3 flex justify-center items-center">
            Page {currentPageNumberValue+1}/{totalPagesValue}
        </div>
        <div class="col-span-3 flex justify-start">
            {#if currentPageValue.hasNext}
                <Button on:click={next}>Next</Button>
            {/if}
        </div>
    </div>

    <div class="col-span-3 flex justify-end">
        <Button on:click={reset}>Read another story</Button>
    </div>
</div>