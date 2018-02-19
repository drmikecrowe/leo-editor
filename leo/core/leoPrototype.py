# -*- coding: utf-8 -*-
#@+leo-ver=5-thin
#@+node:ekr.20180217083023.1: * @file leoPrototype.py
#@@first
'''
Commands that run various prototype projects.

The docstrings for various commands are reference documentation.
'''
import leo.core.leoGlobals as g
# import os
#@+others
#@+node:ekr.20180218012825.1: ** @g.command('leo-cljs')
@g.command('leo-cljs')
@g.command('proto-leo-cljs')
def proto_leo_cljs(event):
    '''
    Vitalije's clojurescript project, using electron and Om/React.
    See #733 for how to build and run this project.
    
    **Summary**
    
    - Build the app *once*: `leocljs>lein descjop-once-dev`
    - Run the app using two *separate* consoles:

        Console 1: `leocljs>lein descjop-figwheel`
            - A prompt will appear when the app loads.
            - Close console 1 *after* closing console 2.
    
        Console2:  `leocljs>electron app/dev`

    **Settings**
        
    @string leo-cljs-base = None
    
        The path to the **base directory**, the leo-el-vue folder.
        
        Defaults to leo/proto/Vitalije/leocljs
        
    @data leo-el-vue-commands
    
        The body text of this setting contains the commands to be executed,
        one per line, from the base directory. Preceding any command with
        '&' causes Leo not to wait for the result.
        
        Defaults to `&lein figwheel`
    '''
    c = event and event.get('c')
    base_dir = g.os_path_finalize_join(g.app.loadDir,
        '..', 'proto', 'Vitalije', 'leocljs')
    g.execute_shell_commands_with_options(
        c = c,
        base_dir=base_dir,
        commands = ['&lein figwheel',],
        command_setting = 'leocljs-commands',
            # @data leo-el-vue-commands
        path_setting= 'leocljs-base',
            # @string leo-el-vue-base
    )
#@+node:ekr.20180217083208.1: ** @g.command('leo-el-vue')
@g.command('leo-el-vue')
@g.command('proto-leo-el-vue')
def proto_leo_el_vue(event):
    '''
    Vitalije's electron/vue project: Leo in CoffeeScript and Vue.
    
    First announced here:
    https://groups.google.com/d/msg/leo-editor/Isd93qGd-RU/SaQoVv7gCQAJ
    
    Original sources and documentation here:
    https://leoelvue.computingart.net/home
    
    The following settings affect this command, with the defaults as shown:
        
    @string leo-el-vue-base = None
    
        The path to the **base directory**, the leo-el-vue folder.
        
        Defaults to leo/proto/Vitalije/leo-el-vue
        
    @data leo-el-vue-commands
    
        The body text of this setting contains the commands to be executed,
        one per line, from the base directory. Preceding any command with
        '&' causes Leo not to wait for the result.
        
        Defaults to &npm run dev
        
        `yarn dev` is faster. `npm -g yarn` installs yarn globally.
    '''
    c = event and event.get('c')
    base_dir = g.os_path_finalize_join(g.app.loadDir,
        '..', 'proto', 'Vitalije', 'leo-el-vue')
    g.execute_shell_commands_with_options(
        c = c,
        base_dir=base_dir,
        commands = ['&npm run dev',],
        command_setting = 'leo-el-vue-commands',
            # @data leo-el-vue-commands
        path_setting= 'leo-el-vue-base',
            # @string leo-el-vue-base
    )
#@+node:ekr.20180217093505.1: ** @g.command('leoserver')
@g.command('leoserver')
@g.command('proto-leo-server')
def proto_leoserver(event):
    '''
    Terry's "fully functional Leo web interface :-)
    
    First announced here, in a comment to #684:
    https://github.com/leo-editor/leo-editor/issues/684#issuecomment-363992724

    The code is here:
    https://github.com/leo-editor/leo-editor/files/1705639/leoserver.zip
    
    The following settings affect this command, with the defaults as shown:
        
    @string leoserver-base = None
    
        The path to the **base directory**, the leo-el-vue folder.
        
        Defaults to leo/proto/Terry/leoserver
        
    @data leo-el-vue-commands
    
        The body text of this setting contains the commands to be executed,
        one per line, in the base directory. Preceding any command with '&'
        causes Leo not to wait for the result.
        
        Defaults to &python leoserver.py
    '''
    c = event and event.get('c')
    base_dir = g.os_path_finalize_join(g.app.loadDir,
        '..', 'proto', 'Terry', 'leoserver')
    g.execute_shell_commands_with_options(
        c = c,
        base_dir=base_dir,
        commands = ['&python leoserver.py',],
        command_setting = 'leoserver-commands',
            # @data leoserver-commands
        path_setting= 'leoserver-base',
            # @string leoserver-base
    )

#@+node:ekr.20180218232508.1: ** @g.command('leovue')
@g.command('leovue')
@g.command('proto-leovue')
def proto_leovue(event):
    '''
    Joe Orr's prootype of Leo using vue.js.

    **Building instructions**
    
        See #735: https://github.com/leo-editor/leo-editor/issues/735

    **@settings**
        
        @string leovue-base = None
        
            The path to the **base directory**, the top-level leovue folder.
            There is no default. You must set this setting.
            
        @data leo-el-vue-commands
            
            Defaults to &npm run dev
    '''
    c = event and event.get('c')
    g.execute_shell_commands_with_options(
        c = c,
        base_dir=None,
        commands = ['&npm run dev',],
        command_setting = 'leovue-commands',
            # @data leovue-commands
        path_setting= 'leovue-base',
            # @string leovue-base
    )
#@-others
#@-leo
