import Vue from 'vue';
import { ApolloClient, createNetworkInterface } from 'apollo-client';
import VueApollo from 'vue-apollo';


const networkInterface = createNetworkInterface({
  uri: (BACKEND_URL || 'http://localhost:8000') + "/graphql/",
  opts: {
    credentials: 'same-origin'
  }
});

const apolloClient = new ApolloClient({
  networkInterface
});

Vue.use(VueApollo);

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
});

export default apolloProvider;
