## RecyclerView使用DataBinding
 具体DataBinding怎么配置以及它的基础用法这里也就不做笔记了。
基础用法可以看一下慕课网的这两节视频
 + **传送门**
  1. [慕课网视频-Android Data Binding实战-入门篇](http://www.imooc.com/learn/719)
  2. [慕课网视频-Android Data Binding实战-高级篇](http://www.imooc.com/learn/720)

在RecyclerView中使用DataBinding首先得创建他们的布局，一级它们的实体类，这里是RecyclerView的基础知识，也不再做笔记

创建完成后首先要把item的布局包裹在\<layout\>\</layout\>里面
就想这样
```xml
<layout>
 	<data>
        <import type="android.view.View"/>
        <import type="com.mengfly.todo.utils.date.DateTools" />

        <variable
            name="item"
            type="com.mengfly.todo.service.entity.TODOItem" />
    </data>

    <LinearLayout
        ...
        >

        <android.support.v7.widget.AppCompatCheckBox
            ...
            android:id="@+id/item_todo_is_done"
            android:visibility="@{item.deleteable ? View.VISIBILE : View.GONE}" />
    </LinearLayout>
</Layout>
```
完成之后，就开始处理ViewHolder
因为对应于RecyclerView里面的item的个数是不一定的，因此我们要使用DataBinding对每一个Item的View进行处理的话，就必须吧Holder和Databinding结合在一起
代码如下：
```java
class ItemHolder extends RecyclerView.ViewHolder {
        private ItemTodoBinding mBinding;

        public ItemHolder(ItemTodoBinding binding) {
            super(binding.getRoot());
            mBinding = binding;
        }

        public ItemTodoBinding getBinding() {
            return mBinding;
        }
    }
```
这样我们让每一个Holder持有一个binding对象，使用这个binding对象就可以访问到界面的元素了

在Adapter里面我们在onCreateViewHolder里面对Binding和Holder进行绑定
```java
@Override
    public ItemHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        ItemTodoBinding binding = DataBindingUtil.inflate(mInflater, R.layout.item_todo, parent, false);
        return new ItemHolder(binding);
    }
```
这样每一个holder就会持有一个binding对象
获取holder对象后我们就可以通过adapter的onBindViewHolder方法给界面绑定数据
```java
 @Override
    public void onBindViewHolder(ItemHolder holder, int position) {
        TODOItem item = mAdapterList.get(position);
        holder.mBinding.setVariable(BR.item, item);
    }
```
这里通过setVariable对变量（在Xml里面的data标签里面定义的变量）进行赋值，这里使用setVariable方法是因为如果我们的RecyclerView的绑定的item不是一个界面，而是根据type的值动态加载的不同界面，那么通过setVarable方法我们也就不用判断到底是哪一个item的界面，通过id就可以直直接赋值，只要这几个item界面的变量的名称都叫item即可

当然如果想要给item里面的子view设置点击事件的话，可以通过binding获取View后直接设置，例如想上面id为item_todo_is_done的CheckBox设置点击事件，就可以这样
```java
holder.mBinding.itemTodoCheckbox.setOnCheckedChangeListener(...)
```

+ 具体的代码可以参考
 [MainItemAdapter.java](https://github.com/MengFly/todo/blob/master/app/src/main/java/com/mengfly/todo/utils/adapter/MainItemAdapter.java)
 [item_todo.xml](https://github.com/MengFly/todo/blob/master/app/src/main/res/layout/item_todo.xml)

