import axios from 'axios'
import Axios from 'axios';

const tasks = {
  state: {
    ftask: '',
    tasks: []
  },

  getters: {
    ftask: state => state.ftask,
    allTasks: state => {
      return state.tasks ? state.tasks : null
    },

  },
  mutations: {
    getTasks: (state, payload) => {
      state.tasks = payload;
      // console.log(payload);
      // console.log(state.tasks)
    }
  },

  actions: {
    getAllTasks: async (context) => {
      let data = await Axios.get('http://localhost:8000/tasks/')
      // console.log(data)
      // console.log(data.data)
      context.commit('getTasks', data)

    }
  },

}

export default tasks
