# Android小知识

[TOC]

## **怎么打开App**[已解决]
> 类似一个桌面应用，通过点击App的图标进入应用

```java
PackageManager packageManager = getPackageManager();
Intent intent = packageManager.getLaunchIntentForPackage(packageInfo.getPackageName());
startActivity(intent);
```





## **RecyclerView怎么设置OnItemClickListener**[已解决]
> Recycle里面没有setOnItemClickListener这个方法，那么要怎么设置呢？不会是在Adapter里面设置吧！
网上的解决方案是放在Adapter里面
可以在Adapter里面封装一个Listener
或者是封装一个OnItemClickListener继承自RecyclerView.OnItemTouchListener

```java
public class RecyclerItemClickListener implements RecyclerView.OnItemTouchListener {

	private GestureDetector mGestureDetector;
	private OnItemClickListener mListener;

	public RecyclerItemClickListener(Context context, OnItemClickListener listener) {
		mListener = listener;
		this.mGestureDetector = new GestureDetector(context, new GestureDetector.SimpleOnGestureListener() {
			@Override
			public boolean onSingleTapUp(MotionEvent e) {
				return true;
			}
		});
	}

	public interface OnItemClickListener {
		void onItemClick(View view, int position);
	}

	@Override
	public boolean onInterceptTouchEvent(RecyclerView rv, MotionEvent e) {
		View childView = rv.findChildViewUnder(e.getX(), e.getY());
		if (childView != null && mListener != null && mGestureDetector.onTouchEvent(e)) {
			mListener.onItemClick(childView, rv.getChildLayoutPosition(childView));
			return true;
		}
		return false;
	}

	@Override
	public void onTouchEvent(RecyclerView rv, MotionEvent e) {
	}

	@Override
	public void onRequestDisallowInterceptTouchEvent(boolean disallowIntercept) {
	}
}
```

## **怎么设置ActionBar的Alpha**[已解决]
在设置ActionBar颜色的时候设置颜色透明度就可以了
即：设置他的colorPrimary属性即可


## **怎么将Menu里面的Icon显示出来**[已解决]
> 在Menu里面的Icon默认是显示不出来的，怎么通过反射将Icon显示出来

```java
//在AppCompatActivity里面用这个方法
@Override
    protected boolean onPrepareOptionsPanel(View view, Menu menu) {
        if (menu != null) {
            if (menu.getClass().getSimpleName().equals("SubMenuBuilder")) {
                try {
                    Method method = menu.getClass().getMethod("setOptionalIconsVisible", boolean.class);
                    method.setAccessible(true);
                    method.invoke(menu, true);
                } catch (Exception e) {
                    Log.e(TAG, "onPrepareOptionsPanel: ", e);
                }
            }
        }
        return super.onPrepareOptionsPanel(view, menu);
    }

//在普通的Activity里面使用这个方法
@Override  
public boolean onMenuOpened(int featureId, Menu menu) {
    if (featureId == Window.FEATURE_ACTION_BAR && menu != null) {
        if (menu.getClass().getSimpleName().equals("MenuBuilder")) {
            try {  
                Method m = menu.getClass().getDeclaredMethod("setOptionalIconsVisible", Boolean.TYPE);  
                m.setAccessible(true);  
                m.invoke(menu, true);  
            } catch (Exception e) {  
            }  
        }  
    }  
    return super.onMenuOpened(featureId, menu);  
}

```

## **各个文件夹下面的AppIcon的尺寸**[已解决]
- **xxxhdpi:**==192 X 192==
- **xxhdpi:**==144 X 144==
- **xhdpi:**==96 X 96==
- **hdpi:**==72 X 72==
- **mdpi:**==48 X 48==
