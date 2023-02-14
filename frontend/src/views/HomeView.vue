<template>
  <div class="home-view">
    <label for="file-upload" class="custom-file-upload"> Upload Files </label>
    <input
      id="file-upload"
      ref="fileInput"
      type="file"
      accept="image/jpeg, image/png, image/jpg"
      multiple
      @change="addURLsToList"
    />
    <div class="images-display" v-if="imageURLs.length">
      <div class="sorting">
        <TilesLg
          class="tile"
          :class="{ active: imagesLarge }"
          @click="() => (imagesLarge = true)"
        />
        <TilesSm
          class="tile"
          :class="{ active: !imagesLarge }"
          @click="() => (imagesLarge = false)"
        />
      </div>
      <div class="images" :class="{ 'tiles-large': imagesLarge }">
        <img
          v-for="imageURL in imageURLs"
          :src="imageURL"
          alt="image"
          class="image"
          :class="{ big: imagesLarge }"
        />
        <img :src="blob" alt="" v-if="blob" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import TilesLg from "@/components/icons/TilesLg.vue";
import TilesSm from "@/components/icons/TilesSm.vue";
import axios from "axios";

const fileInput = ref<HTMLInputElement>();
const imageURLs = ref<string[]>([]);
const imagesLarge = ref(true);
const blob = ref("");

async function addURLsToList() {
  if (fileInput.value) {
    const files = fileInput.value.files;
    if (files) {
      const URLs = [...files].map((file) => URL.createObjectURL(file));
      imageURLs.value = imageURLs.value.concat(URLs);
      let formData = new FormData();
      [...files].forEach((file) => {
        formData.append("images", file);
      });

      const response = await axios.post(
        "http://127.0.0.1:8000/api/",
        formData,
        {
          headers: { "content-type": "multipart/form-data" },
          responseType: "blob",
        }
      );

      blob.value = URL.createObjectURL(response.data);
    }
  }
}
</script>

<style scoped lang="scss">
.home-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  padding: 40px 0;

  .custom-file-upload {
    display: block;
    background-color: $color-orange;
    border-radius: 5px;
    padding: 10px;
    cursor: pointer;

    &:hover {
      opacity: 0.9;
    }
  }

  input[type="file"] {
    display: none;
  }

  .images-display {
    .sorting {
      display: flex;
      justify-content: flex-end;
      width: 100%;
      gap: 5px;
      margin-bottom: 10px;

      .tile {
        opacity: 0.5;
        cursor: pointer;

        &.active {
          opacity: 1;
        }
      }
    }
    .images {
      display: grid;
      grid-template-columns: 2fr;
      justify-items: center;
      gap: 2.5px;

      .image {
        width: 128px;
        height: 128px;
        display: block;
        cursor: pointer;
        background-size: cover;
        background-position: center center;

        &.big {
          width: 256px;
          height: 256px;
        }
      }

      &.tiles-large {
        grid-template-columns: 1fr;
        gap: 5px;
      }
    }
  }
}

@include media-xs {
  .home-view {
    .images-display {
      .images {
        grid-template-columns: repeat(4, 1fr);
        &.tiles-large {
          grid-template-columns: repeat(2, 1fr);
        }
      }
    }
  }
}

@include media-md {
  .home-view {
    .images-display {
      .images {
        grid-template-columns: repeat(6, 1fr);
        &.tiles-large {
          grid-template-columns: repeat(3, 1fr);
        }
      }
    }
  }
}

@include media-lg {
  .home-view {
    .images-display {
      .images {
        grid-template-columns: repeat(8, 1fr);
        &.tiles-large {
          grid-template-columns: repeat(4, 1fr);
        }
      }
    }
  }
}

@include media-xl {
  .home-view {
    .images-display {
      .images {
        grid-template-columns: repeat(10, 1fr);
        &.tiles-large {
          grid-template-columns: repeat(5, 1fr);
        }
      }
    }
  }
}
</style>
