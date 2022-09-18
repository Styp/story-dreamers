<script>
    import {currentPage, currentPageNumber, reset_story, text, totalPages, preloadImages} from "../stores.ts";
    import Button from "./Button.svelte";
    import Booklet from "./Booklet.svelte";

    preloadImages.subscribe(() => {})

    async function reset(){
        reset_story()
    }
</script>

<div class="grid grid-cols-12 gap-8 items-center ">
    <div class="col-span-12 pt-12">
        <Booklet></Booklet>
    </div>

    <div class="col-span-12 flex justify-center">
        <Button on:click={reset}>Read another story</Button>
    </div>
</div>