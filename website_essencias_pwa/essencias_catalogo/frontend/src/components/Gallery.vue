<template>
  <div class="gallery__base">
    <div v-if="loading">
      Loading...
    </div>
    <div v-if="error">
      Couldn't fetch list of products for this catalogue from server...
    </div>
    <div v-if="collection && products && products.images.length > 0" class="gallery__container">
      <h2 class="gallery__title">{{
        products.fields[`name_${$store.getters.lang}`] }}
        ({{collection.fields[`name_${$store.getters.lang}`]}})
        </h2>
        <h3 class="gallery__desc">
          {{products.fields[`description_${$store.getters.lang}`] }}
        </h3>
      <div class="gallery__buttons">
        <a class="gallery__button gallery__button--download"
          :href="`${API_URL}/downloadProduct?productId=${
            id}&productImage=${selectedProduct}`"
          download>Download {{photoDownload[$store.getters.lang]}}</a>
        <a class="gallery__button gallery__button--download"
          :href="`${API_URL}/downloadCollection?lang=${
            $store.getters.lang}&collectionId=${collection.pk}`"
        >Download {{collectionDownload[$store.getters.lang]}}</a>
        <a class="gallery__button gallery__button--download"
          :href="`${API_URL}/downloadGallery?lang=${
            $store.getters.lang}&productId=${id}`"
        >Download {{collectionGallery[$store.getters.lang]}}</a>
        <a class="gallery__button" @click="$router.push(({ path: '/catalogue' }))">
          {{menuButton[$store.getters.lang]}}</a>
      </div>
      <div class="gallery__imageContainer">
        <img class="gallery__image"
          :src="`${API_URL}/${products.images[selectedProduct].url}`"
          :alt="products.fields[`name_${$store.getters.lang}`]"
        />
      </div>

      <ul class="gallery__list">
        <li class="gallery__listItem"
          v-for="(product, index) in products.images" :key="index"
          @click="selectedProduct=index"
        >
          <img
            :src="`${API_URL}/${product.url}`"
            :alt="products.fields[`name_${$store.getters.lang}`].url"
          />
        </li>
      </ul>
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
    selectedProduct: 0,
    API_URL,
    photoDownload: {
      pt: 'Foto',
      en: 'Photo',
      fr: 'Image',
    },
    collectionDownload: {
      pt: 'Coleção',
      en: 'Collection',
      fr: 'Collection',
    },
    collectionGallery: {
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
  computed: {
    products() {
      return this.$store.getters.getProductById(this.id);
    },
    collection() {
      return this.$store.getters.getCollectionByProductId(this.id);
    },
  },
  created() {
    this.requestProducts();
  },
  methods: {
    requestProducts() {
      if (!this.collection) {
        fetch(`${API_URL}/product_collection?productId=${this.id}`)
          .then(res => res.json())
          .then((res) => {
            this.loading = false;
            this.$store.commit('appendCollection', res);
          }).catch((err) => {
            this.loading = false;
            this.error = true;
            throw new Error(err);
          });
      }
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

  &__desc {
    margin: 0 auto;
    text-align: center;
    width: 90%;
    font-size: .9rem;
    color: #000;
    padding-top: 10px;
    padding-bottom: 20px;
    font-weight: 300;

    text-align: justify;
    font-style: italic;
    font-size: 1rem;
    max-width: 700px;

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
    background-color: #BAAC83;
    font-size: 13px;
    border-radius: 15px;
    color: white;
    cursor: pointer;
    text-transform: uppercase;
    padding: 10px 0;
    width: 180px;
    text-decoration: none;
    transition: all .2s ease-in-out;
    border: solid 1px white;

    &:hover {
      color: #BAAC83;
      background: white;
      border: solid 1px #BAAC83;
    }

    &--download {
      background: white;
      color: #BAAC83;
      border-color: #BAAC83;
      border: solid 1px;
      transition: all .2s ease-in-out;

      @include breakpoint-from(mq4) {
        margin-bottom: 10px;
      }

      &:hover {
        color: white;
        border-color: #BAAC83;
        background: #BAAC83;
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
