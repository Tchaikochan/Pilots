        from browser import document, console, alert

        def show(e):
            console.log(e)
            alert('Sou Linda!')
            document['hello'] <= 'Seu lugar é no museu!'

        document['alert-btn'].bind('click', show)