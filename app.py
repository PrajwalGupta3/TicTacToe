from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the board
def create_board():
    return [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

board = create_board()
current_winner = None

# Check for victory
def check_winner(board, sign):
    for row in board:
        if all(cell == sign for cell in row):
            return True
    for col in range(3):
        if all(row[col] == sign for row in board):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    global board, current_winner

    if request.method == 'POST' and 'player1' in request.form:
        session['player1'] = request.form['player1']
        session['symbol'] = request.form['symbol']
        session['computer_symbol'] = 'O' if session['symbol'] == 'X' else 'X'
        board = create_board()
        current_winner = None
        return redirect(url_for('index'))

    elif request.method == 'POST' and 'position' in request.form:
        position = int(request.form['position']) - 1
        row, col = divmod(position, 3)

        if board[row][col] not in ['X', 'O']:
            board[row][col] = session['symbol']
            if check_winner(board, session['symbol']):
                current_winner = session['player1']
            else:
                empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] not in ['X', 'O']]
                if empty_cells:
                    comp_row, comp_col = empty_cells[0]
                    board[comp_row][comp_col] = session['computer_symbol']
                    if check_winner(board, session['computer_symbol']):
                        current_winner = 'Computer'
                else:
                    current_winner = 'Tie'

    return render_template('index.html', board=board, winner=current_winner)

@app.route('/restart', methods=['GET'])
def restart():
    global board, current_winner
    session.clear()
    board = create_board()
    current_winner = None
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
