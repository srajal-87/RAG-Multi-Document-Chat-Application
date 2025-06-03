css = '''
<style>
/* Chat container styling */
.chat-message {
    padding: 1rem;
    margin: 0.5rem 0;
    border-radius: 10px;
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
    max-width: 100%;
}

/* User message styling - aligned to right */
.chat-message.user {
    background-color: #e3f2fd;
    margin-left: 15%;
    flex-direction: row-reverse;
}

/* Bot message styling - aligned to left */
.chat-message.bot {
    background-color: #f5f5f5;
    margin-right: 15%;
}

/* Avatar styling */
.avatar {
    font-size: 1.5rem;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.avatar.user {
    background-color: #2196f3;
    color: white;
}

.avatar.bot {
    background-color: #4caf50;
    color: white;
}

/* Message content styling */
.message-content {
    flex: 1;
    line-height: 1.5;
    color: #333;
    word-wrap: break-word;
}

/* Source info styling */
.source-info {
    font-size: 0.9rem;
    color: #666;
    font-style: italic;
    margin-top: 0.5rem;
    padding-top: 0.5rem;
    border-top: 1px solid #ddd;
}

/* Dark mode support (optional) */
@media (prefers-color-scheme: dark) {
    .chat-message.user {
        background-color: #1e3a8a;
        color: white;
    }
    
    .chat-message.bot {
        background-color: #374151;
        color: white;
    }
    
    .message-content {
        color: inherit;
    }
    
    .source-info {
        color: #9ca3af;
        border-top-color: #4b5563;
    }
}
</style>
'''

# User message template
user_template = '''
<div class="chat-message user">
    <div class="avatar user">👤</div>
    <div class="message-content">{{MSG}}</div>
</div>
'''

# Bot message template  
bot_template = '''
<div class="chat-message bot">
    <div class="avatar bot">🤖</div>
    <div class="message-content">{{MSG}}</div>
</div>
'''