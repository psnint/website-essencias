import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    lang: 'pt',
    catalogue: undefined,
    collections: undefined,
  },
  mutations: {
    changeLanguage(state, lang) {
      state.lang = lang;
    },
    updateCatalogue(state, catalogue) {
      state.catalogue = catalogue;
    },
    appendCollection(state, collection) {
      if (state.collections === undefined) {
        state.collections = {};
      }
      const myCollection = {};
      myCollection[collection.pk] = collection;
      state.collections = {
        ...state.collections,
        ...myCollection,
      };
    },
  },
  getters: {
    lang: state => state.lang,
    catalogue: (state) => {
      const { catalogue } = state;
      return !catalogue ? [] : catalogue.map((entry) => {
        const entryFields = entry.fields;
        entryFields.pk = entry.pk;
        entryFields.image = `media/${entry.fields.image}`;
        return entryFields;
      });
    },
    collections: state => state.collections,
    // eslint-disable-next-line
    collection: state => (id) => {
      return (!state.collections || (state.collections && !(id in state.collections)))
        ? []
        : state.collections[id].products.map((entry) => {
          const entryFields = entry.fields;
          entryFields.pk = entry.pk;
          entryFields.image = `${entry.images[0]}`;
          entryFields.productImages = entry.images;
          return entryFields;
        });
    },
    collectionExists: state => id => Boolean(state.collections) && id in state.collections,
    getProductById: state => (id) => {
      let product;
      const keys = Object.keys(state.collections);
      for (let i = 0; i < keys.length; i += 1) {
        const collection = state.collections[keys[i]];
        const { products } = collection;
        product = products.find(el => el.pk.toString() === id);
        if (product) {
          break;
        }
      }
      return product;
    },
    getCollectionByProductId: state => (id) => {
      let col;
      const keys = Object.keys(state.collections);
      for (let i = 0; i < keys.length; i += 1) {
        const collection = state.collections[keys[i]];
        const { products } = collection;
        if (products.find(el => el.pk.toString() === id)) {
          col = parseInt(keys[i], 10);
          break;
        }
      }
      return (!state.collections || (state.collections && !(col in state.collections)))
        ? undefined
        : state.collections[col];
    },
  },
});
