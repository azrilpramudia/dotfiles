" --- Plugin ----
call plug#begin()

" Theme & UI
Plug 'catppuccin/vim', { 'as': 'catppuccin' }
Plug 'vim-airline/vim-airline'
Plug 'ryanoasis/vim-devicons'

" Navigation
Plug 'preservim/nerdtree'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }

" Tools
Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app && npx --yes yarn install' }
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'sheerun/vim-polyglot'
Plug 'jiangmiao/auto-pairs'
Plug 'airblade/vim-gitgutter'

call plug#end()

" --- Shortcut ----
" Press CTRL+N to open/close folder explorer
nnoremap <C-n> :NERDTreeToggle<CR>

" --- Basic view ---
syntax on
set number
set relativenumber
set cursorline
set notermguicolors

if $TERM == 'xterm-kitty'
  let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
  let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
  set termguicolors
endif

set fillchars=eob:-

" Colors
highlight LineNr ctermfg=grey guifg=#808080
highlight CursorLineNr ctermfg=yellow guifg=#FFFF00
colorscheme catppuccin_macchiato

" --- Tab & Indentation ---  
set tabstop=4
set shiftwidth=4
set expandtab

" --- Additional Feature ---  
set mouse=a
set clipboard=unnamedplus
set ignorecase
set smartcase
