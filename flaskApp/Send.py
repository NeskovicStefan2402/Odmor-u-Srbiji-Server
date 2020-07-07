from flaskApp import socketio,bus

class SendClass:

    @bus.on('evaluate')
    def signUp(data,sid):
        print('Evaluate')
        socketio.emit('eval',data,room=sid)
    
    @bus.on('confirmEvaluation')
    def signUpEval(data,sid):
        print('confirmEvaluation')
        socketio.emit('confirmEvaluation',data,room=sid)
    
    @bus.on('evaluateLogin')
    def evaluateLogin(data,sid):
        print('evaluateLogin')
        socketio.emit('evaluateLogin',data,room=sid)
    
    @bus.on('evaluateLogout')
    def evaluateLogout(data,sid):
        print('evaluateLogout')
        socketio.emit('evaluateLogout',data,room=sid)
    
    @bus.on('sponsorsResp')
    def sponsorsResp(data,sid):
        print('sponsors')
        socketio.emit('responseSponsors',data,room=sid)

    @bus.on('eventsResp')
    def eventsResp(data,sid):
        socketio.emit('responseEvents',data,room=sid)