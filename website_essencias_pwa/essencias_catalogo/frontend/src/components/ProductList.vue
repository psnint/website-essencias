<template>
  <section class="productList__base">
    <div v-if="loading">
      Loading...
    </div>
    <div v-if="error">
      Couldn't fetch list of catalogues from server...
    </div>
    <div v-if="!collectionId || collectionExists" >
      <h2 v-if="isCollection" class="productList__title">{{title}}</h2>
      <h2 v-if="isCollection" class="productList__desc">{{description}}</h2>
      <ul class="productList__list">
        <ProductEntry v-for="product in products" :key="product.pk" :pk="product.pk"
                :title="product[`name_${$store.getters.lang}`]" :imgSrc="`${!collectionId ?
                  product.image : product.productImages[0].url}`"
                :link="`${!collectionId ? 'collection' : '/productDetail'}/${product.pk}`"
                :isProduct="Boolean(collectionId)" :productImages="product.productImages"
                />
      </ul>
    </div>
  </section>
</template>

<script>

import ProductEntry from './ProductEntry.vue';
import API_URL from '../configs';

export default {
  name: 'ProductList',
  props: ['collectionId', 'isCollection'],
  components: {
    ProductEntry,
  },
  data() {
    return {
      loading: false,
      error: null,
      // products: null,
    };
  },
  created() {
    this.requestProducts();
  },
  computed: {
    products() {
      return !this.collectionId
        ? this.$store.getters.catalogue
        : this.$store.getters.collection(this.collectionId).products;
    },
    title() {
      return this.isCollection
        ? this.$store.getters.collection(this.collectionId).fields[`name_${this.$store.getters.lang}`]
        : '';
    },
    description() {
      return this.isCollection
        ? this.$store.getters.collection(this.collectionId).fields[`description_${this.$store.getters.lang}`]
        : '';
    },
    collectionExists() {
      return this.$store.getters.collectionExists(this.collectionId);
    },
  },
  methods: {
    requestProducts() {
      this.error = null;
      this.loading = true;
      // catalogue view
      if (!this.collectionId) {
        // if catalogs not fetched yet
        if (this.products.length < 1) {
          fetch(`${API_URL}`)
            .then(res => res.json())
            .then((res) => {
              this.loading = false;
              this.$store.commit('updateCatalogue', res);
            }).catch(() => {
              this.loading = false;
              this.error = true;
            });
        } else {
          this.loading = false;
        }
      // collection view
      } else if (!this.collectionExists) {
        fetch(`${API_URL}/collection/?collectionId=${this.collectionId}`)
          .then(res => res.json())
          .then((res) => {
            this.loading = false;
            this.$store.commit('appendCollection', res);
          }).catch((err) => {
            this.loading = false;
            this.error = true;
            throw new Error(err);
          });
      } else {
        this.loading = false;
      }
    },
  },
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import "../css/default.scss";

  $moduleName: 'productList';

  .#{$moduleName} {
    &__base {

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
      margin: 20px auto;
      text-transform: uppercase;
      font-size: 1rem;
      width: 90%;

      @include breakpoint-from(mq3) {
        font-size: 1.4rem;
      }
    }

    &__list {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(50%, 1fr));
      grid-column-gap: 7px;
      max-width: 1024px;
      margin: 0 auto;
      padding: 0 7px;

      @include breakpoint-from(mq2) {
        grid-template-columns: repeat(auto-fit, minmax(40%, 1fr));
      }
      @include breakpoint-from(mq3) {
        grid-template-columns: repeat(auto-fit, minmax(30%, 1fr));
      }
      @include breakpoint-from(mq4) {
        grid-template-columns: repeat(auto-fit, minmax(20%, 1fr));
      }
    }
  }

</style>
