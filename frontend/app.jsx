import React from 'react'
import ReactDOM from 'react-dom'
import './style.scss'


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

class Picture extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      text: '',
      formFile: null
    }

  }

  handleImageChange (e) {
    e.preventDefault()
    let data = new FormData()
    data.append('file', e.target.files[0])
    const url = '/api/core/'
    try {
        let csrftoken = getCookie('csrftoken')
        fetch(url, {
          headers: {
            'X-CSRFToken': csrftoken
          },
          credentials: 'same-origin',
          method: 'POST',
          body: data
        })
          .then(response => {
            if (response.status == 201) {
              response.json().then((data) => {
                this.setState({text: data.category})
                console.log('response', data.category)
            })
            }
          })
      } catch (err) {
        console.log('Error during fetching!', err)
      }
  }

  render () {
      return (
          <div className='container py-4'>
            <div className='row center-block py-4'>
                {!this.state.text ?
                     <div className='width'>
                        <h2 className='text-center py-4'> Выбери фотографию и я скажу что на ней. </h2>
                    </div> :
                    <div className='width'>
                      <h2 className='text-center py-4'> Я думаю это  {this.state.text}. Сыграем еще раз? </h2>
                    </div>


                }
             <div className="center-block py-4">
                <div className="file-field">
                  <div className="btn btn-danger btn-lg">
                        <span>Загрузи фотографию</span>
                        <input
                            type='file'
                            id='InputFile'
                            onChange={this.handleImageChange.bind(this)}
                        />
                  </div>
                </div>
             </div>
            </div>
          </div>
      )
  }

}




ReactDOM.render(
  <Picture />,
  document.querySelector('#loloolo')
)
