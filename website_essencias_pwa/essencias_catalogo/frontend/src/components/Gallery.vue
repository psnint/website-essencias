<template>
  <div class="gallery__base">
    <div v-if="loading">
      Loading...
    </div>
    <div v-if="error">
      Couldn't fetch list of products for this catalogue from server...
    </div>
    <div v-if="products.length > 0" class="gallery__container">
      <h2 class="gallery__title">{{
        products[selectedProduct].fields[`name_${$store.getters.lang}`] }}
        ({{collection[`name_${$store.getters.lang}`]}})</h2>
      <div class="gallery__buttons">
        <a class="gallery__button gallery__button--download"
          :href="`${API_URL}/media/${products[selectedProduct].fields.image}`"
          download>Download {{photoDownload[$store.getters.lang]}}</a>
        <a class="gallery__button gallery__button--download"
          :href="`${API_URL}/downloadCollection?lang=${$store.getters.lang}&collectionId=${id}`"
        >Download {{collectionDownload[$store.getters.lang]}}</a>
        <a class="gallery__button" @click="$router.push(({ path: '/catalogue' }))">
          {{menuButton[$store.getters.lang]}}</a>
      </div>
      <div class="gallery__imageContainer">
        <img class="gallery__image"
          :src="`${API_URL}/media/${products[selectedProduct].fields.image}`"
          :alt="products[selectedProduct].fields[`name_${$store.getters.lang}`]"
        />
      </div>

      <ul class="gallery__list">
        <li class="gallery__listItem"
          v-for="(product, index) in products" :key="product.pk"
          @click="selectedProduct=index"
        >
          <img
            :src="`${API_URL}/media/${product.fields.image}`"
            :alt="product.fields[`name_${$store.getters.lang}`]"
          />
        </li>
      </ul>
    </div>
    <div v-else>
      <h2>No Products</h2>
    </div>
  </div>
</template>

<script>
import API_URL from '../configs';

export default {
  name: 'Gallery',
  props: {
    id: {
      type: String,
    },
  },
  data: () => ({
    loading: false,
    error: null,
    products: [],
    collection: {},
    selectedProduct: 0,
    API_URL,
    photoDownload: {
      pt: 'Foto',
      en: 'Photo',
      fr: 'Image',
    },
    collectionDownload: {
      pt: 'Galeria',
      en: 'Gallery',
      fr: 'Galerie',
    },
    menuButton: {
      pt: 'Menu Inicial',
      en: 'Home Menu',
      fr: 'Menu d\'Accueil',
    },
  }),
  created() {
    this.requestProducts();
  },
  methods: {
    requestProducts() {
      this.error = null;
      this.loading = true;
      fetch(`${API_URL}/collection/?collectionId=${this.id}`)
        .then(res => res.json())
        .then((res) => {
          this.loading = false;
          this.products = res.products;
          this.collection = res.fields;
        }).catch(() => {
          this.loading = false;
          this.error = true;
        });
    },
  },
};

</script>


<style scoped lang="scss">
@import "../css/default.scss";

$moduleName: "gallery";

.#{$moduleName} {
  &__base {
    position: relative;
    max-width: 768px;
    width: 100%;
    margin: auto;
  }

  &__title,
  &__image {
    display: inline-block;
    text-align: center;
    width: 80%;
    margin: auto;
  }

  &__title {
    color: #000;
    font-weight: 300;
    margin: 20px 0;
    text-transform: uppercase;
    font-size: 1rem;
    width: 90%;

    @include breakpoint-from(mq3) {
      font-size: 1.4rem;
    }
  }
  &__imageContainer {
    width: 60%;
    min-height: 460px;
    position: relative;
    margin: auto;
    @include breakpoint-to(mq3) {
      min-height: 60vw;
    }
  }
  &__image {
    width: 100%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  &__container {
    width: 100%;
  }

  &__list {
    width: 90%;
    list-style-type: none;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    align-items: center;
  }

  &__listItem {
    width: 21%;
    cursor: pointer;

    img {
      width: 100%;
    }
  }

  &__buttons {
    position: absolute;
    right: -100px;
    display: flex;
    flex-direction: column;

    @include breakpoint-to(mq3) {
      position: relative;
      margin: auto;
      display: flex;
      width: 100%;
      left: 0;
      right: 0;
      flex-direction: row;
      justify-content: space-evenly;
      flex-wrap: wrap;
    }
  }

  &__button {
    background-color: #d9ab2b;
    font-size: 13px;
    border-radius: 15px;
    color: white;
    cursor: pointer;
    text-transform: uppercase;
    padding: 10px 0;
    width: 180px;
    text-decoration: none;

    &--download {
      background: white;
      color: #d9ab2b;
      border-color: #d9ab2b;

      @include breakpoint-from(mq4) {
        margin-bottom: 10px;
      }

    }
    &:last-of-type {
      @include breakpoint-from(mq4) {
        margin-top: 20px;
      }
    }

    @include breakpoint-to(mq3) {
      margin-bottom: 10px;
    }
  }


}
</style>
